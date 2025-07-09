import numpy as np

# Madeup values from the book
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

# Weights first to index by the weight sets. If you flip the order, you'll get shape mismatch and errors.
# Visualisation: https://youtu.be/tMrbN67U9d4?t=1112
output = np.dot(weights, inputs) + biases
print(output)  # Should print [4.8, 1.21, 2.385]

# Manual way
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs) # Should print 4.8, 1.21 and 2.385
