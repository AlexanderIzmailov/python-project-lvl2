from gendiff import generate_diff


import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument("-f", "--format", dest="FORMAT", help='set format of output')
args = parser.parse_args()

f1 = args.first_file
f2 = args.second_file


def main():
    generate_diff(f1, f2)


if __name__ == '__main__':
    main()
