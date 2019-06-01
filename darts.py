def canBeScored(n):
    if n <= 20:
        return True
    elif n % 2 == 0 and n <= 40:
        return True
    elif n % 3 == 0 and n <= 60:
        return True
    elif n == 25 or n == 50:
        return True
    else:
        return False

cannotBeScored = []
for a in range(0,60,1):
    if not canBeScored(a):
        cannotBeScored.append(a)

print(cannotBeScored)
