import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="a simple python implementation of the UNIX cat command",
    epilog="built by GDSC Ashesi. \
            You are welcome to modify and reuse this code as needed"
)

parser.add_argument('filename', help="the file to be displayed")  # use this for test-allow multiple files to be read, you'll need to know about Python's kwargs and args
parser.add_argument('-n', '--number', help="the number of bytes to read from the file", type=int)
parser.add_argument('-l', '--lines', help="the number of lines you want to read from the file.", type=int)


# parsing the created arguments for use:
args = parser.parse_args()


def view_file(file, number_of_bytes=0, number_of_lines=0):
    if number_of_bytes:
        with open(args.filename, 'r') as fp:
            print(fp.read(args.number))  # if type is not specified in argument, you'll have to convert the number to an int first before using it in read
    elif number_of_lines:
        # we can also do fp.readlines(args.lines), but it returns a list, and we will 
        # still need to loop
        with open(args.filename, 'r') as fp:
            for i in range(args.lines):
                print(fp.readline())
    else:
        with open(args.filename, 'r') as fp:
            print(fp.read())


if args.number:
    view_file(args.filename, number_of_bytes=args.number)
elif args.lines:
    view_file(args.filename, number_of_lines=args.lines)
else:
    view_file(args.filename)
