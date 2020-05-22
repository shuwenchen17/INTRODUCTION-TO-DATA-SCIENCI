random_integers = []
for i in range(100):
    rand_int = random.randint(1, 1000)
    random_integers.append(rand_int)
random_integers = [random.randint(1, 100) for i in range(20)]
print(random_integers)
is_odd_ints = []
for i in random_integers:
    if i % 2 == 1:
        is_odd_ints.append(True)
    else:
        is_odd_ints.append(False)
print(is_odd_ints)
print("")
is_odd_ints = [True if i % 2 == 1 else False for i in random_integers]
print(is_odd_ints)