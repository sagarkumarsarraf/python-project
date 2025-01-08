class library:
    list_book=[]
    no_of_book=0
    issued_book=[]
    
    
    
    
print("!!!!!!!WELCOME TO LIBRARY MANAGEMENT SYSTEM!!!!!!!!!!!")
print("*****OPERATION*****")  
print("1.ENTER NEW BOOK\n2.ISSUES BOOK\n3.SEARCH BOOK")
print("|****************************************|")
option=input("ENTER:").capitalize()
# a object is for Bachelor's
a=library()
match option:
    case "1":
        a.list_book.append(input("ENTER BOOK NAME:"))
        a.no_of_book = a.no_of_book+1
        print(a.list_book)
    case "2":
        book=a.issued_book.append(input("ENTER BOOK NAME:"))
        a.no_of_book = a.no_of_book-1
        a.list_book.remove(book)
    case "3":
        book=input("ENTER BOOK NAME:")
        if book in a.list_book:
            print("--------BOOK IS AVAILABLE---------")    
        else:
            print("--------BOOK IS NOT AVAILABLE---------") 
        
        
        
        


    
    
    