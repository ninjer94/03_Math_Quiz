import random

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

question = "{} + {}".format(num_1, num_2)
user_ans = int(input("{} = ".format(question)))
answer = eval(question)

print(question)
print(answer)
