from demo.demo_common import build_manifest, verify_manifest, repair_manifest, risk_score, decision_from_score, deploy, certificate, save_json
from certificate import generate_certificate


def run():
    original = build_manifest(
        name='frontend-risky',
        run_as_non_root=False,
        allow_privilege_escalation=True,
        image='nginx:latest',
        read_only_root_fs=False,
    )
    before = verify_manifest(original)
    repaired, actions = repair_manifest(original, before)
    after = verify_manifest(repaired)
    allowed, message = deploy(repaired, after)
    cert = certificate(repaired, 'PASS' if allowed else 'BLOCK', 'Auto-repaired success path')
    result = {
        'step': '02_success_case_with_auto_repair',
        'scenario': 'Success path after repair',
        'manifest_name': repaired['metadata']['name'],
        'before_count': len(before),
        'after_count': len(after),
        'repair_actions': actions,
        'risk_before': risk_score(before),
        'risk_after': risk_score(after),
        'decision_after': decision_from_score(risk_score(after)),
        'deployment_allowed': allowed,
        'message': message,
        'certificate': cert,
    }
    save_json('02_success_case_with_auto_repair.json', result)
    print('=' * 80)
    print('STEP 02 - SUCCESS CASE WITH AUTO-REPAIR')
    print('Manifest:', result['manifest_name'])
    print('Violations before repair:', result['before_count'])
    print('Repair actions:')
    for action in actions:
        print(' -', action)
    print('Violations after repair:', result['after_count'])
    print('Risk reduction:', result['risk_before'], '->', result['risk_after'])
    print('Decision after repair:', result['decision_after'])
    print(result['message'])
    print('Certificate ID:', cert['certificate_id'])
    # 🔽 NEW CODE FOR PDF CERTIFICATE
    pdf_cert = generate_certificate(
        result['manifest_name'],
        result['before_count'],
        result['after_count'],
        result['decision_after']
    )

    print('Certificate PDF generated:', pdf_cert)
    SERVER_IP = "YOUR_EXTERNAL_IP"
    print(f"Download URL: http://{SERVER_IP}:5000/download/{pdf_cert}")
    return result


if __name__ == '__main__':
    run()
