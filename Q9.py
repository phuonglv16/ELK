def converto(n):
    if n>=1 :
        converto(n // 2)
        print(n % 2,end= " ")
converto(10)