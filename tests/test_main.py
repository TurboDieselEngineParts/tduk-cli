import unittest
from unittest.mock import patch
import io
import sys
from src.tduk_cli import main  # Import your CLI's main function


class TestMain(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('sys.argv', ['tduk-cli'])  # No name argument
    def test_main_default(self, stdout):
        main.main()
        self.assertEqual(stdout.getvalue().strip(), "Hello World")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('sys.argv', ['tduk-cli', '--name', 'Ole'])  # With name argument
    def test_main_with_name(self, stdout):
        main.main()
        self.assertEqual(stdout.getvalue().strip(), "Hello Ole")


if __name__ == '__main__':
    unittest.main()
