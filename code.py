a = 2
b = 3
c = 4


def add(x, y):
    return x + y


result = add(a, b)
print("The result of addition is:", result)
result = add(result, c)
print("The final result after adding c is:", result)
