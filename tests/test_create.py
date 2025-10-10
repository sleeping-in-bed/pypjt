"""Tests for project creation command."""

import os
from pathlib import Path

import typer
from conftest import TMP_DIR
from dotenv import load_dotenv
from typer.testing import CliRunner

from pypjt.create import main

load_dotenv()


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


if __name__ == "__main__":
    test_main(TMP_DIR)
