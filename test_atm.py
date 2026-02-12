import unittest
from atm_project import atm_withdrawal
from unittest.mock import patch
import io


class TestATM(unittest.TestCase):

    def test_withdrawal_success(self):
        initial = 500.0
        with patch("builtins.input", return_value="100"), patch(
            "sys.stdout", new=io.StringIO()
        ) as fake_out:
            new_balance = atm_withdrawal(initial)
            self.assertAlmostEqual(new_balance, 400.0)
            self.assertIn("Withdrawal successful", fake_out.getvalue())

    def test_withdrawal_insufficient(self):
        initial = 500.0
        with patch("builtins.input", return_value="2000"), patch(
            "sys.stdout", new=io.StringIO()
        ) as fake_out:
            new_balance = atm_withdrawal(initial)
            self.assertEqual(new_balance, initial)
            self.assertIn("Insufficient funds", fake_out.getvalue())

    def test_withdrawal_invalid_negative(self):
        initial = 500.0
        with patch("builtins.input", return_value="-50"), patch(
            "sys.stdout", new=io.StringIO()
        ) as fake_out:
            new_balance = atm_withdrawal(initial)
            self.assertEqual(new_balance, initial)
            self.assertIn("Invalid amount", fake_out.getvalue())

    def test_withdrawal_non_numeric(self):
        initial = 500.0
        with patch("builtins.input", return_value="abc"), patch(
            "sys.stdout", new=io.StringIO()
        ) as fake_out:
            new_balance = atm_withdrawal(initial)
            self.assertEqual(new_balance, initial)
            self.assertIn("Please enter a valid numerical amount", fake_out.getvalue())


if __name__ == "__main__":
    unittest.main()
