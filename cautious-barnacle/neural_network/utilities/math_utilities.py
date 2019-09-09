import numpy as np


def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))


# Derivative of the sigmoid function.
def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))
