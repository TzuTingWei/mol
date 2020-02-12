"""
Unit and regression test for the mol package.
"""

# Import package, test suite, and other packages as needed
import mol
import pytest
import sys

def test_mol_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mol" in sys.modules
