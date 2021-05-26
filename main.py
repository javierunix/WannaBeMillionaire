import random
import csv

# create a csv file with questions randomly selected 
with open("questions.csv", "rb") as source:
    lines = [line for line in source]
random_choice = random.sample(lines, 3)
with open("random_questions.csv", "wb") as sink:
    sink.write(b"".join(random_choice))

# load the random csv file with questions into a dict
with open('random_questions.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1:5] for rows in reader}


def quizz(question):
    my_list = [0, 1, 2, 3] # list with the number of possible answers
    my_alphabet_list = ["A", "B", "C", "D"]
    for key, value in question.items(): # iterate over dictionary
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
        else:
            print("You lost!!!!!!")
            break

quizz(dict_from_csv)
