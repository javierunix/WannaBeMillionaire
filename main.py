import random
# This is my main script
question1 = {"What is a prokaryotic cell?": ["Cell without differentiated nucleus", "Cell with differentiated nucleus", "Cell able to do photosynthesis", "Cell not able to do photosynthesis"]}

my_list = [0, 1, 2, 3] # list with the number of possible answers
my_alphabet_list = ["A", "B", "C", "D"]
for key, value in question1.items(): # iterate over dictionary
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
        print('Correct!!!')
    else:
        print("Incorrect!!!")    