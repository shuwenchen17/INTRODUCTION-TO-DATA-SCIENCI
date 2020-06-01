# 方法一
from random import sample

n_samples = 0
while True:
    random_integer = sample(range(1, 1001), 1)[0]
    n_samples += 1
    if random_integer % 56 == 0:
        break
print(random_integer)
print(n_samples)
# 方法二
sample_history = []
while True:
    random_integer = sample(range(1, 1001), 1)[0]
    sample_history.append(random_integer)
    if random_integer % 56 == 0:
        break
print(sample_history)
print(len(sample_history))