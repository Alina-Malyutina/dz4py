N = int(input('Enter quantity of bushes in the garden: '))
garden_bed = [int(input('Enter quantity of berries in bushes: ')) for i in range(N)]
summa = []
for i in range(N-1):
    summa.append(garden_bed[i-1]+garden_bed[i]+garden_bed[i+1])
summa.append(garden_bed[N-2]+garden_bed[N-1]+garden_bed[0])
print(max(summa))