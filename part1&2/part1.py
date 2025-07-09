inputs = [5.2, 3.1, 2.1]
weights = [3.5, 5.3, 1.2]
bias = 3

output = 0
for i in range(len(inputs)):
    output += inputs[i] * weights[i]
output += bias
print(output)