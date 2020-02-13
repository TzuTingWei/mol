import mol
import pytest
import numpy as np


@pytest.mark.parametrize("molecule, com, natom",
    [("water", [9.81833333, 7.60366667, 12.673], 3), ("benzene", [-1.4045, 0, 0], 12)],)

def test_read_xyz(molecule, com, natom):
    moldata = mol.data.get_molecule(molecule)
    assert np.allclose(np.mean(moldata["geometry"], axis=0), com)
    assert len(moldata["geometry"]) == natom
    assert len(moldata["symbols"]) == natom

def test_get_molecule_missing():
    with pytest.raises(FileNotFoundError):
        moldata = mol.data.get_molecule("non-existant")
