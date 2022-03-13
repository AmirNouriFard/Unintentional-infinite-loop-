#Unintentional infinite loop

#Wrong Code :
"""
MAX = 20
n = 1
while n <= MAX:
    factor = 1
    print(end=str(n)+': ')
    while factor <= n:
        if n % factor == 0:
            print(factor,end=' ')
            factor += 1
    print()
    n += 1
"""
#correct code
MAX = 20
n = 1
while n <= MAX:
    factor = 1
    print(end=str(n)+': ')
    while factor <= n:
        if n % factor == 0:
            print(factor,end=' ')
        factor += 1
    print()
    n += 1
#output :
"""
1: 1 
2: 1 2
3: 1 3
4: 1 2 4
5: 1 5
6: 1 2 3 6
7: 1 7
8: 1 2 4 8
9: 1 3 9
10: 1 2 5 10
11: 1 11
12: 1 2 3 4 6 12
13: 1 13
14: 1 2 7 14
15: 1 3 5 15
16: 1 2 4 8 16
17: 1 17
18: 1 2 3 6 9 18
19: 1 19
20: 1 2 4 5 10 20
"""