from io import StringIO
import unittest
from unittest.mock import patch
import bf

class HelloWorldTest(unittest.TestCase):
    def test_print_hello_world(self):
        code = """++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++
               .>++.<<+++++++++++++++.>.+++.------.--------.>+.>."""
        expect_output = "Hello World!\n"
        with unittest.mock.patch("sys.stdout", new=StringIO()) as fake_out:
            bf.run(code)
            self.assertEqual(fake_out.getvalue(), expect_output)

if __name__ == "__main__":
    unittest.main()
