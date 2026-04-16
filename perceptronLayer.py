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

    for i in range(len(letters_list)):
        letters_list[i] = letters_list[i]/total

    return letters_list
