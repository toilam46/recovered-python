''' Example to demonstrate how to use unittest framework in Python.
To run:  cd /home/toila/py_cc++_c#/CC++ShellScript_pro/unittest
         python3 basicExample.py '''
import unittest

class TestExample(unittest.TestCase):
    def test_example(self):
        self.assertEqual('foo'.upper(), 'FOO' )

if __name__ == '__main__':
    unittest.main() 