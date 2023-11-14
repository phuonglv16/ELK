def ham(fn,C):
    newC= []
    for x in C:
        newC.append(fn)
    return newC
C=[1,2,3,4,5]
ham(lambda y:y+2,C)
