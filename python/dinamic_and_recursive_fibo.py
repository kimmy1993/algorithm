import time
import random

#recursive
def fibo_recursive(i):
    if i <= 2:
        return 1
    else:
        return fibo_recursive(i-1) + fibo_recursive(i-2)


#dinamic list
fibo = [1,1]

number = random.randrange(1,32)

i = len(fibo)

#dinamic insert
while i < number:
    fibo.append(fibo[i-1] + fibo[i-2])
    i += 1

    
print("dinamic")
print("number : %d"%number + " fibonacci : %d"%fibo[number-1])

#when number is bigger, it need so many time
print("recursive")
print("number : %d"%number + " fibonacci : %d"%fibo_recursive(number))

time.sleep(10)