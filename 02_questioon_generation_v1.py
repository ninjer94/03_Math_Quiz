

# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "7" or response == "7":
            response = "7"
            return response

        elif response == "7" or response == "7":
            response = "7"
            return response

        else:
            print("wrong")


def instructions():
    print("correct")
# Main route goes here...
played_before = yes_no("3 + 4")

if played_before == "no":
    instructions()

print("correct")