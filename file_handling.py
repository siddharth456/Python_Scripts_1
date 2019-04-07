# Demonstrates file handling in python and related operations
# Different modes are read(r),write(w),append(a), both reading and writing(r+)
# file - C:\Users\shruti\Documents\Bunty\test-folder\flavors_description.txt

#testfile=input("Enter a file name to process:")
#file = open(testfile,'r')
#for each in file:
#    print(each.capitalize(),end='')

# Another way to illustrate read mode
#file = open(testfile,'r')
#print(file.read())

# Illustrate read mode characterwise
#print(file.read(20))

# creating a file using write() mode
#file =open('test.txt','w')
#file.write('This is a test file\n')
#file.write('Created with Python in Pycharm IDE\n')
#file.close()

# write mode along with with() function
with open("testfile.txt","w+") as f:
    f.write("Hello World with Python\n")
    f.write("This is a testfile\n")
    data=f.readlines()
    for lines in data:
        word=lines.split()
        print(word)

# Opens a file and appends some data into it
#with open("testfile.txt","a+") as f:
#    data=[i for i in range(1,11)]
#    f.writelines(str(data))




