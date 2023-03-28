N = int(input('Enter quantity of numbers in first set: '))
M = int(input('Enter quantity of numbers in second set: '))
print('Now enter numbers for first set.')
set1 = set([int(input('Enter number:')) for i in range(N)])
print('Now enter numbers for second set.')
set2 = set([int(input('Enter number:')) for i in range(M)])

unique = set1.intersection(set2)
res = sorted(unique)

print(*res)