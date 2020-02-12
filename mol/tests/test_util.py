import mol
import pytest

@pytest.mark.parametrize("point1, point2, bench", [([0,1], [0,0], 1), ([0,2], [0,0], 2),])

def test_distance(point1, point2, bench):
	assert mol.util.distance(point1, point2) == pytest.approx(bench, abs=1.e-3)
def test_distance_failure():
	assert mol.util.distance([0],[3]) != 5

