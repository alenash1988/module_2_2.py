first = 35
second = 45
third = 35
print(first, second, third)
if first == second and second == third:
    print(int(3))
elif first == second or second == third or first == third:
    print(int(2))
else:
    print(int(0))