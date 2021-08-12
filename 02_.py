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

questions_asked = 0
questions_wrong = 0

mode = ""

# Ask user for # of questions, <enter> for infinite mode
questions = num_check("How many questions: ", "")

if questions == "":
    mode = "infinite"
    questions = 5

end_game = "no"
while end_game == "no":

    # questions Heading


    print()
    if mode == "infinite":
        heading = "Continuous Mode: Questions {}".format(questions_asked + 1)
        questions += 1
        print(heading)
    else:
        heading = "Questions {} of {}".format(questions_asked + 1, questions)
        print(heading)
        # if choose == "xxx":
        #     break

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    to_ask = "{} + {}".format(num_1, num_2)
    show_questions = "{} = ".format(to_ask)

    user_ans = num_check(show_questions, "xxx")
    if user_ans == "xxx":
        break

    if user_ans == eval(to_ask):
        print("correct!".format(user_ans))
    else:
        print("Incorrect!".format(user_ans))

    answer = eval(to_ask)
    print("answer: {}".format(answer))

    if questions_asked == questions - 1:
        end_game = "yes"

    questions_asked += 1

print("thank you for playing")
