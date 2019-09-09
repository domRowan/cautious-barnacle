import numpy

# Squish numbers into the range 0-1 
# -ve inputs close to 0
# +ve inputs close to 1
# input: x: vector or numpy array
def sigmoid(x):
    return 1.0/(1+ numpy.exp(-x))

# Look into ReLU Rectified Linear Unit
# This works well for deep networks
# This has mostly replaced use of sigmoid

def sigmoid_derivative(x):
    return x * (1.0 - x)

class neural_network:
    def __init__(self, x, y):
        self.input = x
        self.weights_1 = numpy.random.rand(self.input.shape[1], 4)
        self.weights_2 = numpy.random.rand(4, 1)
        self.y = y
        self.output = numpy.zeros(y.shape)


    def feed_forward(self):
        self.layer_1 = sigmoid(numpy.dot(self.input, self.weights_1))
        self.output = sigmoid(numpy.dot(self.layer_1, self.weights_2))


    def back_propagation(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        weights_2 = numpy.dot(self.layer_1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        weights_1 = numpy.dot(self.input.T,  (numpy.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights_2.T) * sigmoid_derivative(self.layer_1)))
        
        
        # update the weights with the derivative (slope) of the loss function
        self.weights_1 += weights_1
        self.weights_2 += weights_2


if __name__ == "__main__":
    X = numpy.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])

    X_1 = numpy.array([[0,0,1,1],
    [0,1,1,1],
    [1,0,1,1],
    [1,1,1,0]])
    y = numpy.array([[0],[1],[1],[0]])
    nn = neural_network(X_1,y)

    for i in range(1500):
        nn.feed_forward()
        nn.back_propagation()

    print(nn.output)