def encoding():
    print("!!!!!!!!HIDE YOUR Message/Text !!!!!!!!")
    code=input("Enter code:")
    l=len(code)
    print("length",l)
    if l==3:
        secret_code=code[1:]+code[0]
        print("secret code=",secret_code)
    else:
        secret_code=code[::-1]
        print("secret code=",secret_code)
    print("!!!!!!!!!Encoding sucessful!!!!!!!!!")
       
def decoding():
    print("!!!!!!!!CONVERT CIPHER TEXT INTO PLAIN TEXT!!!!!!!!!!!")
    code=input("Enter code:")
    l=len(code)
    if l==3:
        plain_text=code[-1]+code[0:-2]
        print("Plain_text=",plain_text)
    else:
        plain_text=code[::-1]
        print("Plain_text=",plain_text)
    print("!!!!!!!!!Decoding sucessful!!!!!!!!!")
        
print("what you want to do \n1.Encoding \n2.Decoding")
option=int(input("Enter:"))
if option==1:
    encoding()
elif option==2:
    decoding()
else:
    print("!!!!!!!!!!!!ERROR OCCURED EXIT!!!!!!!!!!")    

 