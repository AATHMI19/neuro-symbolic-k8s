import importlib.util
from pathlib import Path
from certificate import generate_certificate

DEMO_DIR = Path(__file__).resolve().parent / 'demo'
FILES = [
    '01_failure_case_without_repair.py',
    '02_success_case_with_auto_repair.py',
    '03_success_case_clean_manifest.py',
    '04_demo_summary.py',
]

def run_file(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    mod.run()

if __name__ == '__main__':
    for file_name in FILES:
        run_file(DEMO_DIR / file_name)
