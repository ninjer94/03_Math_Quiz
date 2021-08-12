# Function used to check input is valid
import random

def num_check(question, exit_code):
    while True:
        response = input(question)


        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != exit_code:
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here

rounds_played = 0
mode = ""

# Ask user for # of rounds, <enter> for infinite mode
rounds = num_check("How many questions: ", "")

if rounds == "":
    mode = "infinite"
    rounds = 5

end_game = "no"
while end_game == "no":

    # Rounds Heading


    print()
    if mode == "infinite":
        heading = "Continuous Mode: Questions {}".format(rounds_played + 1)
        rounds += 1
        print(heading)
    else:
        heading = "Questions {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        # if choose == "xxx":
        #     break

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    question = "{} + {}".format(num_1, num_2)
    display_question = "{} =".format(question)

    user_ans = num_check(display_question, "xxx")
    if user_ans == "xxx":
        break


    answer = eval(question)

    if rounds_played == rounds - 1:
        end_game = "yes"


    # rest of loop / game
    print("You chose {}".format(user_ans))

    rounds_played += 1


print("Thank you for playing")
