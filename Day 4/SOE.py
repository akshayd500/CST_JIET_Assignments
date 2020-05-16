#Sieve of Eratosthenes

def soe(n):
    prime = [True for i in range(n + 1)]
    i = 2
    while (i * i <= n):
        if (prime[i] == True):
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1

    for i in range(2, n + 1):
        if prime[i]:
            print(i,end="   ")

n = int(input("Enter the Range:"))
soe(n)
