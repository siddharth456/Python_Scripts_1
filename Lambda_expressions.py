# Small anonymous functions can be created with the lambda keyword
# Example: lambda a,b:a+b
# The example function returns the sum of two arguments
# lambda functions can have any number of arguments but only a single expression

pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(reverse=True)
print("Sorted in reverse:",pairs)
pairs.sort()
print("Default sorting:",pairs)
pairs.sort(key=lambda pairs:pairs[1])
print("Sorted using lambda function as key:",pairs)
