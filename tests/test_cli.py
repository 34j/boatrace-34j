import subprocess
import sys


def test_add_command():
    """The CLI adds two numbers."""
    result = subprocess.run(
        [sys.executable, "-m", "boatrace_34j", "1", "1"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == "2"
