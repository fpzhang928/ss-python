"""Tests for cli."""
from typer.testing import CliRunner

from serious_scaffold.cli import app

runner = CliRunner()


def test_cli() -> None:
    """Tests for cli."""
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_cli_run() -> None:
    """Tests for run subcommand of the cli."""
    result = runner.invoke(app, "run")
    assert result.exit_code == 0
    assert not result.output
