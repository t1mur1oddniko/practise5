def parrots(n):
    if 10 < n < 20:
        print(n, "попугаев")
    elif n % 10 == 1:  
        print(n, "попугай")
    elif 2 <= n % 10 <= 4: 
        print(n, "попугая")
    else: 
        print(n, "попугаев")

num = int(input())  
parrots(num)