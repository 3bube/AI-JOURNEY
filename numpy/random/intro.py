from numpy import random


x = random.randint(100, size=(5))
y = random.rand()
print(x)
print(y)



from numpy import random

x = random.randint(100, size=(3, 5))

print(x)


from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)



from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)