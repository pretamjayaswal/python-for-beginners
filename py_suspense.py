def cap(inputs=[]):
    inputs.append("some stuff")
    pattern = ["a list based on "] + inputs
    return pattern




print(cap())
print(cap())
print(cap())
print(cap())
print(cap())
print(cap())

# never put multale data types as default parameters in func defn