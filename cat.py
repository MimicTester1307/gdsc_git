import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog="cat",
        description="a simple python implementation of the UNIX cat command",
        epilog="built by GDSC Ashesi. \
                You are welcome to modify and reuse this code as needed"
    )

    parser.add_argument('filename', help="the file to be displayed")  # use this for test-allow multiple files to be read, you'll need to know about Python's kwargs and args

    # Add arguments -n and -l to mutually exclusive groups because they should not be called at the same time
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--number', help="the number of bytes to read from the file", type=int)
    group.add_argument('-l', '--lines', help="the number of lines you want to read from the file.", type=int)


    # parsing the created arguments for use:
    return parser.parse_args()


def view_file(args):
    if args.number:
        with open(args.filename, 'r') as fp:
            print(fp.read(args.number))  # if type is not specified in argument, you'll have to convert the number to an int first before using it in read
    elif args.lines:
        # we can also do fp.readlines(args.lines), but it returns a list, and we will 
        # still need to loop
        with open(args.filename, 'r') as fp:
            for i in range(args.lines):
                print(fp.readline())
    else:
        with open(args.filename, 'r') as fp:
            print(fp.read())

