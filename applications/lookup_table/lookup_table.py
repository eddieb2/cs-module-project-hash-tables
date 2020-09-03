# Your code here
import math
import random
import time

start_time = time.time()

cache = {}

def fill_cache():
    for x in range(2, 14):
        for y in range(3, 6):
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            cache[math.pow(x,y)] = v

def slowfun(x, y):
   result = math.pow(x,y)
   return cache[result]

fill_cache()

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
    time.sleep(0.5)


end_time = time.time()
print(f'Time of program: {end_time - start_time}')

