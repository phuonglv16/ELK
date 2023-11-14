def songuyento(n):
    if n <=1:
        return False
    else :
        for i in range (2,n) :
            if n % i == 0 :
                return False
        return True 
n=0
for i in range(1,1000):
    if songuyento(i):
        n= n + 1
        print("{:>3}".format(str(i)), end= " ")
        if n % 10 == 0:
            print("")
