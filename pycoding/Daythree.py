p="@SuryA123"
u_count=0
l_count=0
s_count=0
n_count=0

if len(p)>=8:
    for i in p:
        if "A"<=i<="Z":
            u_count+=1
        elif "a"<=i<="z":
            l_count+=1
        elif "0"<=i<="9":
            n_count+=1
        else:
            s_count+=1
    result= "valid password" if u_count>=2 and l_count>=2 and s_count>=1 and n_count>=1  else "Invalid password"
    print(result)
else:
    print("Invalid password, check the length of the password")

import random
i=1
while i<10:
    n=int(input("choose your number:"))
    guess=random.randint(1,10)
    if n<guess:
        print("lowest number")
    elif n>guess:
        print("highest number")
    else:
        print("got correctly")
    i+=1