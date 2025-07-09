inputs = [1, 2, 3] # Madeup values from the book
weights = [0.2, 0.8, -0.5] # Madeup values from the book
bias = 2 # Madeup value from the book

output = 0
for i in range(len(inputs)):
    output += inputs[i] * weights[i]
output += bias
print(output) # Should print 2.3