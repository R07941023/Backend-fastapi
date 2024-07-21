floor = 5

res = 0
for n in range(floor):
    if floor-n % 2 == 0:
        res += 1
print(res)