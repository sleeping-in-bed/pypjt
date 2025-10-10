"""Test configuration and fixtures."""

import shutil
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.parent

TESTS_DIR = Path(__file__).parent
RC_DIR = TESTS_DIR / "resources"

TMP_DIR = TESTS_DIR / "tmp"
if TMP_DIR.exists():
    shutil.rmtree(TMP_DIR)
TMP_DIR.mkdir(exist_ok=True)
TMP_FILE = TMP_DIR / "tmp.tmp"
