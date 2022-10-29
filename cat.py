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
