# random numbers!

import random
import numpy as np 
# pip install numpy
# pip3 install numpy for Mac
number = random.randint(1, 20)
print(number)

# generate 100 random numbers
# put therm in a list
# print


listofrandomnumbers = []
for i in range (100):
    n = random.randint(1,20)
    listofrandomnumbers.append (n)

print(listofrandomnumbers)

list2 = [random.randint(1,20) for i in range (100)]
print(list2)
print("length of list2 is", len(list2))
# compute the sum of them
total = 0 # listofrandomnumbers[0] + listofrandomnumbers[1] + ... + listofrandomnumbers [99]
for number in listofrandomnumbers:
    total = total + number
#

totalsum = sum(listofrandomnumbers)
print("total: ", total, totalsum)


# npnumber + np.random

