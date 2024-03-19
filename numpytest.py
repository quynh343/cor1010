import numpy as np

print ('my numpy version: ', np.__version__)

randomList = []
for i in range(1_000_000):
    n = np.random.randint(1,20)
    randomList.append(n)
#
# print("randomList:", randomList)

randomArray = np.random.randint(1, 6, size=10000000)
print("randomArray: ", randomArray.shape, randomArray.size)

count = 0
for number in randomArray:
    #print(number)
    if number == 5:
        count += 1 
#
print("the list contains ", count, "5s")
print(f"the list contains {count} 5s.")

print("Finished")
# let's find out if there is 19 in the list. 


