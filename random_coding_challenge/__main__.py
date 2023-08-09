import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Random Coding Challenge")
parser.add_argument("num", type=int, help="Challenge number")
args = parser.parse_args()

# create a challenge_nn.py file (padded with leading 0)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
challenge_file = os.path.join(BASE_DIR, f"challenge_{args.num:02d}.py")

# if challenge file already exists, exit
if os.path.isfile(challenge_file):
    print(f"Challenge {args.num} already exists")
    sys.exit(1)
else:
    with open(challenge_file, "w") as f:
        f.write(
            f"""
def challenge_{args.num:02d}():
    # add your code here
    pass
    
if __name__ == "__main__":
    # add something to run here if you wish
    pass
"""
        )

# test file
test_file = os.path.join(
    os.path.dirname(BASE_DIR), "tests", f"test_challenge_{args.num:02d}.py"
)
if os.path.isfile(test_file):
    print(f"Test file for challenge {args.num} already exists")
else:
    with open(test_file, "w") as f:
        f.write(
            f"""
from random_coding_challenge.challenge_{args.num:02d} import challenge_{args.num:02d}

def test_challenge_{args.num:02d}():
    # add your tests here
    assert False
"""
        )
