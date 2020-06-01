# 樣本標準差
# 方法一
x = list(range(1, 101))
N = len(x)
x_bar = sum(x) / N
print(x_bar)
sse = 0
for xi in x:
    error = xi - x_bar
    squared_error = (error)**2
    sse += squared_error #sse = sse + squared_error
sample_mse = sse / (N-1)
sample_stdev = sample_mse**(0.5)
print(sample_stdev)
# 方法二
from statistics import stdev

stdev(range(1, 101)) # [1, 2, 3, ..., 100]