import mol

def test_distance():
	assert mol.util.distance([0,1], [0,2]) == 1
