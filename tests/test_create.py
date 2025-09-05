"""Tests for project creation command."""

import os
import sys
from pathlib import Path

import typer
from typer.testing import CliRunner
from dotenv import load_dotenv

from pypjt.create import main

load_dotenv()
PROJECT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_DIR))


def test_main(tmp_path: Path) -> None:
    """Create a project via CLI and ensure success.

    Args:
        tmp_path: Temporary directory for running the command.

    """
    project_name = "test_project"

    os.chdir(tmp_path)
    app = typer.Typer()
    app.command()(main)
    runner = CliRunner()
    result = runner.invoke(app, input=f"{project_name}\n1.0.0a1\nme\na@a.com\nTest\n")
    print(result.output)
    assert result.exit_code == 0
