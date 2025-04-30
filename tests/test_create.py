import os
import sys
from pathlib import Path

from click.testing import CliRunner
from dotenv import load_dotenv

from pypjt.create import main

load_dotenv()
PROJECT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_DIR))


def test_main(tmp_path):
    project_name = "pypjt"

    os.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(main, input=f"{project_name}\n1.0.0a1\nme\na@a.com\nTest\n")
    print(result.output)
    assert result.exit_code == 0
