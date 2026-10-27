import subprocess
import sys
import unittest
from pathlib import Path

from main import greet


class MainTests(unittest.TestCase):
    def test_custom_name(self):
        self.assertEqual(greet("世界"), "Hello, 世界!")

    def test_script_runs(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("main.py"))],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello, Codex!")


if __name__ == "__main__":
    unittest.main()
