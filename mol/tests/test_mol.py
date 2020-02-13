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

def test_canvas():
    assert mol.canvas()


def test_molecular():
    moldata = mol.Molecule(["He", "He"], [[0,0,0], [0,0,1]])
    assert pytest.approx(1.0) == moldata.distance(0,1)

def test_name_molecule_distance():
    moldata = mol.NamedMolecule("He2", ["He", "He"], [[0,0,0], [0,0,1]])
    assert pytest.approx(1.0) == moldata.distance(0,1)

