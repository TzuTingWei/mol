import numpy as np


def distance(point1, point2):
    """
    Calculate distance between two points.

    Parameters
    -------
    point1 : array_like
        The first point.
    point2 : array_like
        The second point.
    Returns
    -------
    float
        The distance between point1 and point2. 
    """

    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)


def read_xyz(filename):
    """
    Read in the indicated file.

    Parameters
    -------
    filename : string
        The file which contain the atom symbol and geometry.
    Returns
    -------
    np.array
        A np.array of the file.
    """

    with open(filename, "r") as handle:
        data = handle.readlines()

    data = data[2:]
    data = [x.split() for x in data]
    symbols = [x[0] for x in data]
    #xyz = np.array([[float(y) for y in x[1:]] for x in data])
    
    xyz = []
    for line in data:
        xyz.append([float(line[1]), float(line[2]), float(line[3])])

    return {"symbols": np.array(symbols), "geometry": xyz}
