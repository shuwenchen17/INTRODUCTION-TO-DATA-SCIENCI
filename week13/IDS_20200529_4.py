test_str = 'azcbobobegghak'
n_char = len(test_str)
print(n_char)
for i in range(12):
    print(test_str[i:i+3])
  
print("")
test_str = 'azcbobobegghak'
n_char = len(test_str)
n_bobs = 0
for i in range(n_char - 2):
    #print(test_str[i:i+3])
    if test_str[i:i+3] == 'bob':
        n_bobs += 1
print(n_bobs)
