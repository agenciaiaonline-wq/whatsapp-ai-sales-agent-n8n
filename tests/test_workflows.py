import pathlib
import unittest

from scripts.validate_workflows import validate_workflows_dir


class WorkflowValidationTests(unittest.TestCase):
    def test_all_n8n_workflows_valid(self) -> None:
        workflows_dir = pathlib.Path(__file__).resolve().parent.parent / "workflows"
        errors = validate_workflows_dir(workflows_dir)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
