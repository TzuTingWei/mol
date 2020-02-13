import argparse

parser = argparse.ArgumentParser(description='Add some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='interger list')

