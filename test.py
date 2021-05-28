import csv
import random
from art import *

prizes1 = [0, 100, 200, 300, 500, 1000] # first section of prizes
prizes2 = [1000, 2000, 4000, 8000, 16000, 32000] #  second section of prizes
prizes3 = [32000, 64000, 125000, 250000, 500000, 1000000] # third section of prizes

with open('questions.csv', newline='') as f: # load the questions from csv file and save into a list
    reader = csv.reader(f)
    data = list(reader)

header = data[0] # save the first row in a variable

data = data[1:] # delete the header row from the list

data = random.sample(data, len(data)) # resample randomly the data

data_level1 = []
data_level2 = []
data_level3 = []
data_level4 = []
data_level5 = []
level_num = 3 # max number of questions of each dificulty level

for i in range(len(data)):
	if data[i][5] == '1' and len(data_level1) < level_num:
		data_level1.append(data[i])
	elif data[i][5] == '2' and len(data_level2) < level_num:
		data_level2.append(data[i])
	if data[i][5] == '3' and len(data_level3) < level_num:
		data_level3.append(data[i])
	if data[i][5] == '4' and len(data_level4) < level_num:
		data_level4.append(data[i])
	if data[i][5] == '5' and len(data_level5) < level_num:
		data_level5.append(data[i])	

newdata = data_level1 + data_level2 + data_level3 + data_level4 + data_level5
print(len(newdata))