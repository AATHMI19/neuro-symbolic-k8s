from __future__ import annotations
import copy
import hashlib
import json
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parents[1] / 'demo_outputs'
OUTPUT_DIR.mkdir(exist_ok=True)


def build_manifest(name: str, run_as_non_root: bool, allow_privilege_escalation: bool, image: str = 'nginx:latest', read_only_root_fs: bool = False) -> dict:
    return {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {'name': name, 'namespace': 'default'},
        'spec': {
            'replicas': 1,
            'template': {
                'spec': {
                    'containers': [
                        {
                            'name': name,
                            'image': image,
                            'securityContext': {
                                'runAsNonRoot': run_as_non_root,
                                'allowPrivilegeEscalation': allow_privilege_escalation,
                                'readOnlyRootFilesystem': read_only_root_fs,
                            },
                        }
                    ]
                }
            }
        }
    }


def verify_manifest(manifest: dict) -> list[dict]:
    violations = []
    try:
        container = manifest['spec']['template']['spec']['containers'][0]
        sc = container.get('securityContext', {})
        if not sc.get('runAsNonRoot', False):
            violations.append({'rule': 'RunAsNonRoot', 'severity': 'critical', 'message': 'Container can run as root.'})
        if sc.get('allowPrivilegeEscalation', True):
            violations.append({'rule': 'AllowPrivilegeEscalation', 'severity': 'high', 'message': 'Privilege escalation is enabled.'})
        if not sc.get('readOnlyRootFilesystem', False):
            violations.append({'rule': 'ReadOnlyRootFilesystem', 'severity': 'medium', 'message': 'Root filesystem is writable.'})
        if str(container.get('image', '')).endswith(':latest'):
            violations.append({'rule': 'PinnedImageTag', 'severity': 'medium', 'message': 'Image tag is not pinned to an immutable version.'})
    except Exception as exc:
        violations.append({'rule': 'InvalidManifest', 'severity': 'critical', 'message': f'Manifest parsing failed: {exc}'})
    return violations


def risk_score(violations: list[dict]) -> int:
    weights = {'critical': 40, 'high': 30, 'medium': 15, 'low': 5}
    return sum(weights.get(v['severity'], 0) for v in violations)


def decision_from_score(score: int) -> str:
    if score >= 40:
        return 'BLOCK'
    if score >= 20:
        return 'REVIEW'
    if score > 0:
        return 'LOW_RISK'
    return 'PASS'


def repair_manifest(manifest: dict, violations: list[dict]) -> tuple[dict, list[str]]:
    repaired = copy.deepcopy(manifest)
    container = repaired['spec']['template']['spec']['containers'][0]
    sc = container.setdefault('securityContext', {})
    actions = []
    rules = {v['rule'] for v in violations}
    if 'RunAsNonRoot' in rules:
        sc['runAsNonRoot'] = True
        actions.append('Set runAsNonRoot=True')
    if 'AllowPrivilegeEscalation' in rules:
        sc['allowPrivilegeEscalation'] = False
        actions.append('Set allowPrivilegeEscalation=False')
    if 'ReadOnlyRootFilesystem' in rules:
        sc['readOnlyRootFilesystem'] = True
        actions.append('Set readOnlyRootFilesystem=True')
    if 'PinnedImageTag' in rules and str(container.get('image', '')).endswith(':latest'):
        container['image'] = str(container['image']).replace(':latest', ':1.25.3')
        actions.append('Pin image tag to nginx:1.25.3')
    return repaired, actions


def certificate(manifest: dict, status: str, scenario: str) -> dict:
    digest = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
    return {
        'scenario': scenario,
        'status': status,
        'manifest_hash': digest,
        'certificate_id': digest[:16],
        'generated_at': datetime.utcnow().isoformat() + 'Z'
    }


def deploy(manifest: dict, violations: list[dict]) -> tuple[bool, str]:
    score = risk_score(violations)
    decision = decision_from_score(score)
    name = manifest['metadata']['name']
    if decision == 'BLOCK':
        return False, f'DEPLOYMENT BLOCKED for {name} | score={score} | decision={decision}'
    return True, f'DEPLOYMENT ALLOWED for {name} | score={score} | decision={decision}'


def save_json(filename: str, data: dict | list) -> Path:
    path = OUTPUT_DIR / filename
    path.write_text(json.dumps(data, indent=2))
    return path
