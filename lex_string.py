import re


def upp_to_low(org_str):
    regex = "[^A-Za-z]"
    return re.sub(regex, "", org_str.lower())


# step2
def first_occur():
    pass


# Step3
def append_letters():
    pass


def chk_empty_strings():
    pass


def print_str():
    pass


if __name__ == "__main__":
    string = input("Enter a string?")
    new_str = upp_to_low(string)
    letters = sorted(set(new_str))
    listToStr = " ".join([str(elem) for elem in letters])
    print(listToStr)

    print("The string is " + string)
    print("The string is " + new_str)

else:
    print("will do something else here")
