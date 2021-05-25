import random
# This is my main script
question1 = {"What is a prokaryotic cell?": ["A cell without differentiated nucleus", "A cell with differentiated nucleus", "A cell able to do photosynthesis", "A cell not able to do photosynthesis"]}

my_list = [0, 1, 2, 3] # list with the number of possible answers

for key, value in question1.items(): # iterate over dictionary
    print(key) # print the question
    random.shuffle(my_list) # make the list random
    for i in my_list:
        print(value[i])
    