import numpy as np
import random
from utilities.math_utilities import sigmoid, sigmoid_prime


class Network(object):
    """
    The list ``sizes`` contains the number of neurons in the
    respective layers of the network.  For example, if the list
    was [2, 3, 1] then it would be a three-layer network, with the
    first layer containing 2 neurons, the second layer 3 neurons,
    and the third layer 1 neuron.  The biases and weights for the
    network are initialized randomly, using a Gaussian
    distribution with mean 0, and variance 1.  Note that the first
    layer is assumed to be an input layer, and by convention we
    won't set any biases for those neurons, since biases are only
    ever used in computing the outputs from later layers.
    """

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    """
    It is assumed that the input a is an (n, 1) Numpy ndarray,
    not a (n,) vector. Here, n is the number of inputs to the network.
    If you try to use an (n,) vector as input you'll get strange results.
    Although using an (n,) vector appears the more natural choice,
    using an (n, 1) ndarray makes it particularly easy to modify the code
    to feedforward multiple inputs at once, and that is sometimes convenient.
    """
    # Return the output of the network in "a" is input.

    def feedforward(self, a):
        for bias, weight in zip(self.biases, self.weights):
            a = sigmoid(np.dot(weight, a)+bias)
        return a

    """
    Train the neural network using mini-batch sthchastic gradient descent.
    The "training_data" is a list of the tuples "(x, y)" representing the
    training inputs and the desired outputs. The other non-optional parameters are
    self explanitory. If "test_data" is provided then the network will be evaluated
    against the test data after each epoch, and partial progress printed out.
    This is useful for tracking progress, but slows things down substantially.
    eta is the learning rate, η.
    The code works as follows. In each epoch, it starts by randomly shuffling the
    training data, and then partitions it into mini-batches of the appropriate size.
    This is an easy way of sampling randomly from the training data.
    Then for each mini_batch we apply a single step of gradient descent.
    This is done by the code self.update_mini_batch(mini_batch, eta),
    which updates the network weights and biases according to a single iteration of
    gradient descent, using just the training data in mini_batch.
    """

    def stochasticGradientDescent(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        if training_data:
            training_data = list(training_data)
            n = len(training_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {} : {} / {}".format(j,
                                                  self.evaluate(test_data), n_test))
            else:
                print("Epoch {} complete".format(j))

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    """
    Update the network's weights and biases by applying
    gradient descent using backpropagation to a single mini batch.
    The "mini_batch" is a list of tuples "(x, y)", and "eta"
    is the learning rate.
    Most of the work is done by the line
    delta_nabla_b, delta_nabla_w = self.backprop(x, y)
    """

    def update_mini_batch(self, mini_batch, eta):
        # nabla is a symbol used for vector differential operator: ∇
        # In this sense is the standard derivative of the bias and weight
        # bias: ∂Cx/∂blj = ∇b = nabla_b
        # weight: ∂Cx/∂wljk = ∇w = nabla_w
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backpropagation(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    """
    Summary of the 4 equations for back propagation
    
    δL=∇aC⊙σ′(zL).(BP1a)

    δl=((wl+1)Tδl+1)⊙σ′(zl),(BP2)

    ∂C/∂blj=δlj.(BP3)

    ∂C/∂wljk=al−1k δlj.(BP4)

    """

    def backpropagation(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(bias.shape) for bias in self.biases]
        nabla_w = [np.zeros(weight.shape) for weight in self.weights]

        # feedforward
        activations, zs = self.backpropagation_feedforward(x)

        # Compute the output error
        # delta is the output error δl
        delta = self.backpropagation_compute_output_error(activations, zs, y)

        # Use the error to calculate the bias and weight of the last layer

        # list [-1] notation allows you to access the last item in the list
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        # Backpropagate the error from the 2nd to last layer to the first

        return self.backpropagation_backpropagate_error(activations, zs, delta, nabla_b, nabla_w)

    """
    For each layer calculate:
    activation: ax,l=σ(zx,l) 
    z: zl=wlal−1+bl
    
    where, z is the change in a neuron's weighted output
    """

    def backpropagation_feedforward(self, x):
        activation = x
        activations = [x]  # list to store all the activations, layer by layer
        zs = []  # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        return (activations, zs)

    def backpropagation_compute_output_error(self, activations,  zs, y):
        return self.cost_derivative(
            activations[-1], y) * sigmoid_prime(zs[-1])

    def backpropagation_backpropagate_error(self, activations, zs, delta, nabla_b, nabla_w):
        # l = 1 means the last layer of neurons, l = 2 is the second-last layer...
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())

        return (nabla_b, nabla_w)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)
