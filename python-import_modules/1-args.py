import sys

def test_arguments():
    num_arguments = len(sys.argv) - 1 

    if num_arguments == 0:
        print(":")
    else:
        separator = ":"
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}{separator} {arg}")

if __name__ == "__main__":
    test_arguments()
