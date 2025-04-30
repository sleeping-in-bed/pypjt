import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_DIR))

TESTS_DIR = Path(__file__).parent
RC_DIR = TESTS_DIR / "resources"

TMP_DIR = TESTS_DIR / "tmp"
TMP_DIR.mkdir(exist_ok=True)
TMP_FILE = TMP_DIR / "tmp.tmp"
