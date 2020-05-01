x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_counter = 0 # 歸零
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        #odd_counter = odd_counter + 1 # = NOT ==
        odd_counter += 1
    i += 1 # step
print("======")
print(odd_counter)