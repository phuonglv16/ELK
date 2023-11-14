def giaithua(n):
    if n <= 1:
        print("no")
    else :
        return (n * giaithua(n - 1))
giaithua(5)
