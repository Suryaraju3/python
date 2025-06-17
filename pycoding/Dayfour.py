def v_email(func):
    def inner(email):
        if email.endswith('.com') and '@' in email:
            func(email)
        else:
            print('error')
    return inner

@v_email
def mail(email):
    print(email)
mail("surya123@gmail.com")

@v_email
def yahoo(email):
    print(email)
yahoo('surya123yahoo.com')



num=[1,2,3,4,5]
a=[0,2,3]
b=200
n=int(input("number"))
try:
    print(n/2)
    # print(b/0)  
   # print(c) 
    # num[1]
    #num[sue] 
    #c=100/num 
    # a[11]  
except ZeroDivisionError as message:
    print("error: ",message)
except NameError as message:
    print("error:  ",message)
except ValueError as message:
    print("error: ",message)
except IndexError as msg:
    print("error: ",msg)
except AttributeError as msg:
    print("error: ",msg)
finally:
    print("execution...  ")


    