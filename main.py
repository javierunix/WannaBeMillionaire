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


# loop for creating 15 questions from data[1] to data[15] (data[0] is ommited because it is the header)

for k in range(1,16): 
    exec(f'question{k} = Quizz(data[k])')

tprint('Who wants to be a Millionare') # a nice text ;-)


# the function sobera is the responsable for asking questions and evaluating the the answers:
# return True if answer is correct, False if not

def sobera(question):
    my_list = [0, 1, 2, 3] # list with the number of possible answers, that will be reorder randomly
    my_alphabet_list = ["A", "B", "C", "D"] # alphabetic list

    # we create a dictionary, with questions as key and a list with 4 possible answers as value
    my_dict = {question.question : [question.correct_answer, question.incorrect_answer1, question.incorrect_answer2, question.incorrect_answer3]}

    for key, value in my_dict.items(): 

        question_dict={} # dictionary to associate the answer selected with the correct
        print(key) # print the question
        random.shuffle(my_list) # reorder radomly the list of questions
        counter = 0

        for i in my_list:

            print("%s: %s" %(my_alphabet_list[counter], value[i])) # print and alphabetic alement and a question
            question_dict[my_alphabet_list[counter]] = value[i] # associate alphabetic alement and a question
            counter += 1

        my_string = input("Choose the correct answer: ") # ask for a response
        my_string = my_string.upper() # convert the response given to capital

        if question_dict[my_string] == value[0]: # if the letter selected is the associated with the correct answer return True

            print('Correct! You can move on!!!!')
            return True  

        else: # otherwise, return False

            print("You lost!!!!!!")
            return False



move_on = True # one of two exit conditions of the following while loop
number_of_question = 1 
money = 0
consolation_price = 0


while (move_on == True) and (number_of_question < 16): # while contestant gives a correct answer and there are questions left 
    
    tprint('Question Number:' + str(number_of_question))
    exec(f'move_on = sobera(question{number_of_question})') # execute the function sobera on question(number)
                                                            # if answer is correct move_on = True, if incorrect move_on = False

    if move_on: # if anwser correct

        if number_of_question < 6: # while the number of the question is less than six, we apply the first list of prices
            money = prizes1[number_of_question]
            if number_of_question == 5:
                consolation_price = prizes2[0] # once the player hit question 5 he consolidates 1000$ 
            else:
                consolation_price = prizes1[0] # otherwise the player will keep 0$

        elif number_of_question < 11:
            money = prizes2[number_of_question - 5]
            if number_of_question == 10:
                consolation_price = prizes3[0] # once the player hit question 5 he consolidates 32000$ 
            else:
                consolation_price = prizes2[0] #otherwise the player will keep 1000$ 

        elif number_of_question < 16:
            money = prizes3[number_of_question - 10]
            consolation_price = prizes3[0]

        if number_of_question < 15:
            print("Now you have %d$. If you fail the following questions you will keep %d$." %(money, consolation_price))
            you_sure = input("¿Are you sure that you want to continue? ")
            you_sure = you_sure.lower() # ask to the contestant if he want to continue
            if you_sure == 'no' or you_sure == 'n':
                move_on = False # if answer is no, exit while loop
        elif number_of_question == 15:
            tprint('Congratulations!!!')

    else: # if answer is incorrect

        if number_of_question < 6: # if fail before the question 6
            money = prizes1[0] # 0$
        elif number_of_question < 11: # if fail before the question 11
            money = prizes2[0] # 1000$
        elif number_of_question < 16: # if fail before the question 16 
            money = prizes3[0] # 32000$
    number_of_question += 1

tprint('You won:  ' + str(money) + '$')
