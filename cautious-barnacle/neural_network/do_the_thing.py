from data.mnist_loader import load_data_wrapper
from neural_network import Network

# Load_data_wrapper has a hardcoded reference to the mnist data file.
# If you move this file you should update this reference
training_data, validation_input, test_data = load_data_wrapper()

# Hyper parameters
layer_1_hidden_neurons = 784
layer_2_hidden_neurons = 30
layer_3_hidden_neurons = 10
layers = [layer_1_hidden_neurons,
          layer_2_hidden_neurons, layer_3_hidden_neurons]

number_of_epochs = 30
mini_batch_size = 10
learning_rate = 3.0

net = Network(layers)

net.stochasticGradientDescent(
    training_data, number_of_epochs, mini_batch_size, learning_rate, test_data=test_data)
