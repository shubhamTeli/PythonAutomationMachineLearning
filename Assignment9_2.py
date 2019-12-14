"""
Write a program which accept file name from user and open that file and display the contents
of that file on screen
"""
import sys;

def main(fileName):

    with open(fileName) as f:
        print("\nFile contents are:\n\n",f.read());

if __name__ == "__main__":
    main(str(sys.argv[1]));