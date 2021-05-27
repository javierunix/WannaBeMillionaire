import csv
import random

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

# now we create a class for each question
class Quizz1(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)


class Quizz2(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)



class Quizz3(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)



class Quizz4(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)



class Quizz5(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)



class Quizz6(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)



class Quizz7(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)



    def __init__(self, my_list):
        super().__init__(my_list)



class Quizz8(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)



class Quizz9(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)


class Quizz10(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)


class Quizz11(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)


class Quizz12(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)


class Quizz13(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)


class Quizz14(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)

class Quizz15(Quizz):

    def __init__(self, my_list):
        super().__init__(my_list)

# loop for creating all the questions
for k in range(1,6):
    exec(f'question{k} = Quizz{k}(data[k])')

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

if sobera(question1) == True:
    print('hola, mundo')