#------------------------------------------------------------------------------------------------------------------------

import unittest
import pytest
import sys
import os
import pyflakes.api
from pyflakes.reporter import Reporter

@unittest.skipIf(os.getenv('spasdn04', False), 'skipping pyflakes syntax check on Travis')
class PyflakesCheck(unittest.TestCase):
    
    def test_pyflakes_syntax(self) -> None:
        rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pyflakes.api.checkRecursive([rootPath + '/simulators_and_3d/', rootPath + '/tests/'], Reporter(sys.stdout, sys.stderr))

if __name__ == "__main__":
    unittest.main(verbosity=2)