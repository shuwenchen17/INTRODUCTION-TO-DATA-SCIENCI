x = int(input("請輸入一個正整數:"))
divisors = []
for i in range(1, x+1):
    if x % i == 0:
        divisors.append(i)
print(divisors)
n_divisors = len(divisors)
if n_divisors == 2:
    print("{}是質數".format(x))
else:
    print("{}不是質數".format(x))