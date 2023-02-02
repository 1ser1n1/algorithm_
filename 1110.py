N = input()
num = [int(i) for i in N]
count = 0

while True:
    new = [int(j) for j in str(sum(num))]
    sumN = str(int(str(num[-1]) + str(new[-1])))
    count += 1
    if sumN == N:
        break
    num = [int(i) for i in str(sumN)]

print(count)