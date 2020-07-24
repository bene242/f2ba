import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="square the number entered in this pos (positional argument)", type=int)
args = parser.parse_args()
#print(args.echo)
print(args.square**2)
