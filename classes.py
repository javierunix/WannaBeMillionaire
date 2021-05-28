import csv

with open('questions.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


# create the Quizz Superclass
class Quizz:

	def __init__(self, my_list):

		self.question = my_list[0]
		self.correct_answer = my_list[1]
		self.incorrect_answer1 = my_list[1]
		self.incorrect_answer2 = my_list[2]
		self.incorrect_answer3 = my_list[3]

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

print(question1.question)
print(question2.question)
print(question3.question)
print(question4.question)
print(question5.question)


	
