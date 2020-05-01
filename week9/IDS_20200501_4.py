x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_summation = 0 # 歸零
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        odd_summation = odd_summation + i # 數值累加
    i += 1 # step
print("======")
print(odd_summation)