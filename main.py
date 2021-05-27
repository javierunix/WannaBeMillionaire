import csv
import random
from art import *

prizes1 = [0, 100, 200, 300, 500, 1000] # first section of prizes
prizes2 = [1000, 2000, 4000, 8000, 16000, 32000] #  second section of prizes
prizes3 = [32000, 64000, 125000, 250000, 500000, 1000000] # third section of prizes

with open('questions.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


# create the Quizz Superclass
class Quizz:

    def __init__(self, my_list):

        self.question = my_list[0]
        self.correct_answer = my_list[1]
        self.incorrect_answer1 = my_list[2]
        self.incorrect_answer2 = my_list[3]
        self.incorrect_answer3 = my_list[4]


# loop for creating all the questions
for k in range(1,16):
    exec(f'question{k} = Quizz(data[k])')

move_on = True

def sobera(question):
    my_list = [0, 1, 2, 3] # list with the number of possible answers
    my_alphabet_list = ["A", "B", "C", "D"]

    my_dict = {question.question : [question.correct_answer, question.incorrect_answer1, question.incorrect_answer2, question.incorrect_answer3]}

    for key, value in my_dict.items():

        question_dict={}
        print(key) # print the question
        random.shuffle(my_list) # make the list random
        counter = 0

        for i in my_list:

            print("%s: %s" %(my_alphabet_list[counter], value[i]))
            question_dict[my_alphabet_list[counter]] = value[i]
            counter += 1

        my_string = input("Choose the correct answer: ")
        my_string = my_string.upper()

        if question_dict[my_string] == value[0]:

            print('Correct! You can move on!!!!')
            return True

        else:

            print("You lost!!!!!!")
            return False

tprint('Who wants to be a Millionare')
number_of_question = 1
money = 0
while (move_on == True) and (number_of_question <= 16):
    exec(f'move_on = sobera(question{number_of_question})')
    if move_on:
        money = prizes1[number_of_question]
        print("Now you have %d$. If you fail the following questions you will loose everything." %money)
        you_sure = input("¿Are you sure that you want to continue? ")
        you_sure = you_sure.lower()
        if you_sure == 'no' or you_sure == 'n':
            move_on = False
    else:
        money = prizes1[0]
    number_of_question += 1

print(money)
