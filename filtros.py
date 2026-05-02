a=[1,2,3,4,5,6,7,8,9]
def fuc(x):
    return x%2==0
b=list(filter(fuc,a))
print(b)