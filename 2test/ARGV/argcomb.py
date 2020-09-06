import argparse
parser = argparse.ArgumentParser()

parser.add_argument("square", help="number to square", type=int)
parser.add_argument("-v", "--verbose", help="increase verbosity", action="store_true")

args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print("the square of " + str(args.square) + " is " + str(answer))
else:
    print(answer)
