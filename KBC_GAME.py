print("!!!!!!!!!!!!!!WELCOME TO KBC GAME!!!!!!!!!!!!!!!!")
print("****Rules****")
print("YOU WILL BE ASKED 10 QUESTIONS\nEach correct Answer will double your amount")
Amount=500
lifeline=3
A=0
B=1
C=2
D=3
#question input part start here
Question=["Who was the first woman Prime Minister of India?","What is the capital city of Japan?","Which planet is known as the Red Planet?","Who invented the telephone?",
          "What is the smallest country in the world by area?","Which gas is most abundant in the Earth's atmosphere?",
          "In which year did India gain independence?","Who wrote the epic Ramayana?","What is the hardest natural substance on Earth?",
          " Who is known as the Father of Computers?"]
Answer=["Indira Gandhi","Tokyo","Mars","Alexander Graham Bell","Vatican City","Nitrogen","1947","Valmiki","Diamond","Charles Babbage"]
Queoption=[
    ["Indira Gandhi","Sushma swaraj","Nirmala sitharaman","Smrithi Irani"],
    ["Kathmandu","Tokyo","Canberra","New dehli"],
    ["Earth","Juptier","Mercury","Mars"],
    ["Isaac Newton","Alexander Graham Bell","Charles Darwin","Albert Einstein "],
    ["Hum","Vatican City","Adamstown","Durbuy"],
    ["Nitrogen","Oxygen","Argon","Carbon Dioxide"],
    ["1776","1967","1947","1901"],
    ["Rabindranath Tagore", "Mulk Raj Anand", "Chetan Bhagat", "Valmiki"],
    ["Gypsum", "Apatite","Diamond", "Corundum"],
    ["Wright Brothers","Vint Cerf and Bob Kahn","Charles Babbage","Louis Pasteur"]
    
    
    ]

#Game logic start from here
print("your the question is on the screen")
print("\n\n")
for i in range(0,10):
    print(Question[i])
    print("\n\n")
    option=Queoption[i]
    for j in range(0,4):
        print(option[j])
        print("\n")
    print("*********GIVE YOUR ANSWER**********")
    x=input("Enter:")
    if x=="A":
        ans=0
    elif x=="B":
        ans=1
    elif x=="C":
        ans=2
    else:
        ans=3
    print(ans)
    if option[ans]==Answer[i]:
        Amount=Amount*2
        print("----------------This is the correct Ansewer--------------------")
        print("your Amount=",Amount)
        print("you have lifeline=",lifeline)
        print("-----------NEXT QUESTION is on the screen-------------")
    else:
        lifeline=lifeline-1;
        print("-------SORRY YOUR ANSWER IS WORNG----------")
        print("you have lifeline=",lifeline)
        print("Your Amount =",Amount)
        print("-----------NEXT QUESTION is on the screen-------------")
    if lifeline==0:
      
        break
    else: 
        continue
print("Lifeline=",lifeline)
print("!!!!!!!!!!!GAME OVER!!!!!!!!!!")
print("__TOTAL AMOUNT YOU WIN___=",Amount)          
        
        
    




