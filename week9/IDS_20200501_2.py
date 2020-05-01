x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        print(i)
    i += 1 # step