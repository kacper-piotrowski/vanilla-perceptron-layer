import os
from random import shuffle

class Perceptron:
    def __init__(self, weights_length, bias, alpha,beta = None):
        self.weights_length = weights_length
        self.bias = bias
        self.alpha = alpha
        self.beta = beta if beta is not None else alpha
        self.weights = [0 for i in range(weights_length)]
        self.initial_bias = bias
    def classify(self, x_vector):
        net = 0
        for i in range(len(self.weights)):
            net += self.weights[i] * x_vector[i]
        net -= self.bias
        return 1 if net > 0 else 0
    def classify_net(self, x_vector):
        net = 0
        for i in range(len(self.weights)):
            net += self.weights[i] * x_vector[i]
        net -= self.bias
        return net
    def learn(self, x_vector, d):
        updated_weights = self.weights.copy()
        dy = (d-self.classify(x_vector))
        for i in range(len(self.weights)):
            updated_weights[i] += self.alpha * dy * x_vector[i]
        self.weights = updated_weights
        self.bias = self.bias - (dy * self.beta)
    def reset(self):
        self.weights = [0 for i in range(self.weights_length)]
        self.bias = self.initial_bias

def get_letters_list(text):
    letters_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    text = text.lower().strip()
    total = 0

    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122:
            total += 1
            letters_list[ord(text[i])-97] = letters_list[ord(text[i])-97] + 1

    if total > 0:
        for i in range(len(letters_list)):
            letters_list[i] = letters_list[i] / total

    return letters_list

languages = os.listdir("training_data")
bias = float(input("Enter bias: "))
alpha = float(input("Enter the learning rate (alpha): "))
perceptron_dict = {}
training_set = []

for language in languages:
    perceptron_dict[language] = Perceptron(26,bias,alpha)
    text_files = os.listdir("training_data/" + language)
    for file in text_files:
        if file.endswith(".txt"):
            with open(os.path.join("training_data/" + language + "/" + file), "r", encoding="utf-8") as f:
                file_text = f.read()
                training_set.append([get_letters_list(file_text),language])

learncycles = int(input("Enter the number of epochs: "))

for i in range(learncycles):
    shuffle(training_set)
    for j in range(len(training_set)):
        vector = training_set[j][0]
        correct_language = training_set[j][1]
        for language in perceptron_dict:
            if language == correct_language:
                perceptron_dict[language].learn(vector,1)
            else:
                perceptron_dict[language].learn(vector,0)

def classify_language(user_text):
    user_vector = get_letters_list(user_text)
    answers = []
    for language in perceptron_dict:
        answers.append([perceptron_dict[language].classify_net(user_vector),language])
    answers.sort(key=lambda x: x[0], reverse=True)
    return answers[0][1]

def classify_test_folder():
    test_set_answers=[]

    text_files = os.listdir("test_data/")
    for file in text_files:
        if file.endswith(".txt"):
            with open(os.path.join("test_data/"+ file), "r", encoding="utf-8") as f:
                file_text = f.read()
                classification = classify_language(file_text)
                test_set_answers.append([f.name, classification])

    return test_set_answers

def classify_user_file(file_name):
    try:
        with open(os.path.join(file_name), "r" , encoding="utf-8") as file:
            file_text = file.read()
            classification = classify_language(file_text)
            return classification
    except FileNotFoundError:
        return -1

program_mode = -1
while program_mode != "0":
    print("Choose an option: ")
    print("1- Classify the test folder")
    print("2- Classify a user text input")
    print("3- Classify a single user file")
    print("0- Exit")
    program_mode = input("Choice: ")
    if program_mode == "1":
        answers = classify_test_folder()
        for answer in answers:
            print(f"File: {answer[0]}, classification: {answer[1]}")
        input("Press Enter to continue...")
    elif program_mode == "2":
        user_text = input("Text: ")
        answer = classify_language(user_text)
        print(f"Your classification is: {answer}")
        input("Press Enter to continue...")
    elif program_mode == "3":
        user_file = input("Enter the file name: ")
        answer = classify_user_file(user_file)
        if answer != -1:
            print(f"Your classification is: {answer}")
        else:
            print("File not found!")
        input("Press Enter to continue...")