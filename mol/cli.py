import argparse
from .util import read_xyz, distance

def main():
	parser = argparse.ArgumentParser(description='A Molecule utility that reads XYZ files and calculates the distance between atoms at index1 and index2.')
	parser.add_argument('filename', type=str, help='The XYZ file to read.')
	parser.add_argument('index1', type=int, help='Index of the first atom.')
	parser.add_argument('index2', type=int, help='Index of the second atom.')

	args = parser.parse_args()
	print(args)

	moldata = read_xyz(args.filename)
	print(f"Reading XYZ file: {args.filename}")
	#print("Reading XYZ file:{}".format(args.filename))
	#print(moldata)

	print("Calculating distance...")

	dist = distance(moldata["geometry"][args.index1], moldata["geometry"][args.index2])

	s1 = moldata["symbols"][args.index1]
	s2 = moldata["symbols"][args.index2]
	
	print(f"Distance between atoms {args.index1}:{s1} and {args.index2}:{s2} = {dist:.3f}Å")



