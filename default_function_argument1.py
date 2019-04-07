# the default argument is evaluated only once
#i=6
#def f(arg=i):
#    print(arg)
#i=60
#f() Output in this case is 6

# However there is a difference when the default is a mutable object such as list or dictionary or instance of most classes
# In below example the function accumulates the arguments passed to it on subsequent calls
def f(a,L=[]):
    L.append(a)
    return L
#print(f(1))
#print(f(2))
#print(f(3))
for i in range(1,10):
    print(f(i))