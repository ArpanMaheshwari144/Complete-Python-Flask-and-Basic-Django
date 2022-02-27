# Creating a Command Line Utility and make a faulty calculator
import argparse
import sys

def calc(args):
    if args.x == 45.0 and args.y == 3.0 and args.o =="mul":
        return 555

    elif args.x == 56 and args.y == 9 and args.o =="add":
        return 77

    elif args.x == 56  and args.y == 6 and args.o =="div":
        return 4

    elif args.o =='add':
        return args.x + args.y

    elif args.o =='sub':
        return args.x - args.y

    elif args.o =='mul':
        return args.x * args.y

    elif args.o =='div':
        return args.x / args.y
    else:
        return "something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='calculater')
    parser.add_argument('--x', type=float, default=1.0,
                         help='enter 1st number, help calculation')

    parser.add_argument('--y', type=float, default=1.0,
                       help='enter 2nd number, help calculation')

    parser.add_argument('--o', type=str, default='add',
                       help='operator, help calculation')

    args =parser.parse_args()
    sys.stdout.write(str(calc(args)))