numbers = [10, 5, 7, 2, 1]
"""
for x in numbers:
    print(x)
#for(int i;i<numbers.size();i++)
for i in range(0,len(numbers),1):
    print(i,numbers[i])

for i in range((len(numbers)-1),-1,-1):
    print(i,numbers[i])

print("-2:",numbers[-2])

print("sebelum:",numbers,"panjangnya:",len(numbers))
numbers[1] = numbers[4]
del numbers[2]
print("sesudah:",numbers,"panjangnya:",len(numbers))"""

from random import randint
"""
for x in range(100):
    numbers.append(randint(1,23))
    """
for x in range(100):
    numbers.insert(0,x)
    
num2 = []
for x in range(100):
    num2.append(randint(1,23))

numbers.extend(num2)

print("sesudah part 2:",numbers,"panjangnya:",len(numbers))
