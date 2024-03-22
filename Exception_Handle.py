# exception is nothing but Runtime error and it occure due to incorrect implentation of logic
# Exception Handing is a mechanism through which we can handle the Runtime error usingg following
# try, except, else

a= int(input("Enter First number :"))
s= int(input("Enter Second number :"))
try:
    c=a/s
    print("first number divide by second number is ", c)
except:
    print('can not devide by 0')
print("End of Program")

