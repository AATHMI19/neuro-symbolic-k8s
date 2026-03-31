from demo.demo_common import build_manifest, verify_manifest, risk_score, decision_from_score, deploy, save_json


def run():
    manifest = build_manifest(
        name='frontend-risky',
        run_as_non_root=False,
        allow_privilege_escalation=True,
        image='nginx:latest',
        read_only_root_fs=False,
    )
    violations = verify_manifest(manifest)
    allowed, message = deploy(manifest, violations)
    result = {
        'step': '01_failure_case_without_repair',
        'scenario': 'Failure path',
        'manifest_name': manifest['metadata']['name'],
        'violations': violations,
        'risk_score': risk_score(violations),
        'decision': decision_from_score(risk_score(violations)),
        'deployment_allowed': allowed,
        'message': message,
    }
    save_json('01_failure_case_without_repair.json', result)
    print('=' * 80)
    print('STEP 01 - FAILURE CASE WITHOUT REPAIR')
    print('Manifest:', result['manifest_name'])
    print('Violations detected:', len(violations))
    for item in violations:
        print(f" - [{item['severity'].upper()}] {item['rule']}: {item['message']}")
    print('Risk score:', result['risk_score'])
    print('Decision:', result['decision'])
    print(result['message'])
    return result


if __name__ == '__main__':
    run()
