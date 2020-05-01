x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_summation = 0 # 歸零
odd_counter = 0
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        odd_counter += 1
        odd_summation += i # 數值累加
        print("現在的整數次:{}, 奇數計數為{}個, 總合為{}".format(i, odd_counter,odd_summation))
    else:
        print("現在的整數次:{}, 奇數計數為{}個, 總合為{}".format(i, odd_counter,odd_summation))    
    i += 1 # step
print("======")
print(odd_counter)
print(odd_summation)