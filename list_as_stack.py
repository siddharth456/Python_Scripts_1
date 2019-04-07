# The list methods make it easy to use a list as a stack where the last element added is the first element retrieved
# i.e Last In First Out(LIFO)
# To add an item to the top of the stack,use the append() method.
# To retrieve an item from the top of the stack,use the pop() method without an explicit index

stack=['a','e','i','o']
stack.append('u')
print(stack)
print(stack.pop())