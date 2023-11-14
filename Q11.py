def mydef(fn,c):
    redual=0
    for i in c :
        redual=fn(redual,i)
    return redual
A=[1,2,3,4,5]
mydef=(lambda x,y:x+y,A))