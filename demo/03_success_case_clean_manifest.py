from demo.demo_common import build_manifest, verify_manifest, risk_score, decision_from_score, deploy, certificate, save_json
from certificate import generate_certificate

def run():
    manifest = build_manifest(
        name='payments-compliant',
        run_as_non_root=True,
        allow_privilege_escalation=False,
        image='nginx:1.25.3',
        read_only_root_fs=True,
    )
    violations = verify_manifest(manifest)
    allowed, message = deploy(manifest, violations)
    cert = certificate(manifest, 'PASS' if allowed else 'BLOCK', 'Already compliant success path')
    result = {
        'step': '03_success_case_clean_manifest',
        'scenario': 'Direct success path',
        'manifest_name': manifest['metadata']['name'],
        'violations': violations,
        'risk_score': risk_score(violations),
        'decision': decision_from_score(risk_score(violations)),
        'deployment_allowed': allowed,
        'message': message,
        'certificate': cert,
    }
    save_json('03_success_case_clean_manifest.json', result)
    print('=' * 80)
    print('STEP 03 - SUCCESS CASE WITH CLEAN MANIFEST')
    print('Manifest:', result['manifest_name'])
    print('Violations detected:', len(violations))
    print('Risk score:', result['risk_score'])
    print('Decision:', result['decision'])
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
