import random as r
import string as s
import argparse


def check(numbers, checkDigit=False):
    """Check the card number's validness"""

    numberList = []  # Each number in 'number' arg
    oddPositionList = []  # List that contains items in odd position
    evenPositionList = []  # List that contains items in even position
    numbers = str(numbers)
    if numbers.isdigit() or type(numbers) == int and numbers is not None:
        nNumber = len(numbers)
        for i in str(numbers[::-1]):  # Reverse the 'numbers'
            numberList.append(i)

        for pos, item in enumerate(numberList):
            if (pos % 2 != 0):  # If item is in odd position (1,3,5,7..)
                m = (int(item) * 2)
                if (m >= 10):
                    # There must be a better way of doing this
                    mStr = str(m)
                    mList = []
                    mList.append(int(mStr[0]))
                    mList.append(int(mStr[1]))
                    oddPositionList.append(sum(mList))
                else:
                    oddPositionList.append(m)
            else:  # If item is not in odd position (0,2,4,6..)
                evenPositionList.append(int(item))

        sumOfLists = sum(oddPositionList) + sum(evenPositionList)

        # TODO: Check digit integration is required
        if checkDigit:  # If check digit is added
            if (sumOfLists % 10 == 0):
                return True
            else:
                return False
        else:  # If check digit is not added
            if (sumOfLists % 10 == 0):
                return True
            else:
                return False
    else:
        print("Please use digits. Example: 79927398713")


def generate(size, showOutput=False):
    """Generate a random valid card"""

    while True:
        firstDigit = str(r.randrange(1, 9))  # Don't start with 0
        otherDigits = "".join(r.choices(s.digits, k=size-1))
        numbers = (firstDigit + otherDigits)

        if check(numbers):
            print("Found a valid card number: ", numbers)
            return False
        else:
            if showOutput:
                print(numbers)
            else:
                continue


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="luhn.py",
        allow_abbrev=False,
        description=" ## Luhn Algorithm ## ",
        epilog="Example: luhn.py generate 16")

    parser.version = "0.2"

    parser.add_argument("--generate", "-g",
                        metavar="length",
                        type=int,
                        help="generate a random valid card",
                        dest="generate")

    parser.add_argument("--check", "-c",
                        metavar="numbers",
                        type=int,
                        help="check the card number's validness",
                        dest="check")

    parser.add_argument("-v", "--version", action="version")

    args = parser.parse_args()
    # if args.generate and args.check is None:  # I don't know how to to this
    #     print("luhn.py -h for more info")
    if args.generate is not None and args.generate >= 2:
        generate(args.generate)
    elif args.generate is not None and args.generate < 2:
        print(f"{args.generate} is invalid. Use 2 or higher.")
    elif args.check is not None and args.check >= 2:
        if check(args.check):
            print("This is a valid card.")
        else:
            print("This is not a valid card.")
    elif args.check is not None and args.check < 2:
        print(f"{args.generate} is invalid. Use 2 or higher.")
