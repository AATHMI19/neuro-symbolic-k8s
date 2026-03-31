import importlib.util
from pathlib import Path
from demo.demo_common import OUTPUT_DIR, save_json

THIS_DIR = Path(__file__).resolve().parent

FILES = [
    '01_failure_case_without_repair.py',
    '02_success_case_with_auto_repair.py',
    '03_success_case_clean_manifest.py',
]


def _load_and_run(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.run()


def run():
    results = [_load_and_run(THIS_DIR / name) for name in FILES]
    lines = []
    lines.append('# Demo Execution Summary\n')
    lines.append('| Step | Scenario | Manifest | Violations / Before→After | Risk | Decision | Deployment |')
    lines.append('|---|---|---|---|---:|---|---|')
    for item in results:
        if 'before_count' in item:
            viol = f"{item['before_count']} -> {item['after_count']}"
            risk = f"{item['risk_before']} -> {item['risk_after']}"
            decision = item['decision_after']
        else:
            viol = str(len(item.get('violations', [])))
            risk = str(item['risk_score'])
            decision = item['decision']
        deploy = 'Allowed' if item['deployment_allowed'] else 'Blocked'
        lines.append(f"| {item['step']} | {item['scenario']} | {item['manifest_name']} | {viol} | {risk} | {decision} | {deploy} |")

    lines.append('\n## Demo speaking flow')
    lines.append('1. Run Step 01 to show a visible blocked deployment failure.')
    lines.append('2. Run Step 02 to show auto-repair turning the same risky manifest into a compliant deployment.')
    lines.append('3. Run Step 03 to show a clean manifest passing directly without repair.')
    lines.append('4. Use this summary table to close the demo with both failure and success visibility.')
    summary_text = '\n'.join(lines) + '\n'
    (OUTPUT_DIR / 'demo_execution_summary.md').write_text(summary_text, encoding='utf-8')
    save_json('demo_execution_summary.json', results)
    print('=' * 80)
    print('STEP 04 - SUMMARY GENERATED')
    print(summary_text)
    return results


if __name__ == '__main__':
    run()
