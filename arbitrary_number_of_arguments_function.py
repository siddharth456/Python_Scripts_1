# We can pass any number of arguments to the function like this
# Only keyword arguments can be used after *args parameter
def concat(*args,sep='/'):
    return sep.join(args)
print(concat('earth','mars'))
print(concat('earth','mars','venus'))
print(concat('earth','mars','venus',sep='$'))


