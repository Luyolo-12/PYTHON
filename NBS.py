#Lets build Robot NDONDOZI!!!
print('Hello, welcome to ZONDI BUTCHERY!!\n')

name = input('What is your name?\n')

if name == 'Msanda' or name == "Njabulo" or name == "Rolland":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))

    if evil_status == 'Yes' and good_deeds < 4:
       print ('You are not welcome here ' + name + '. Get out you evil person!!!!')
       exit()
    else:
        print("So you are one of those good " + name + ", come on in!!")
else:
    print('Hello ' + name + ', thank you so much for coming in today!!\n')
    
    
menu = 'Beef Sausages, Mnandi Mince meat, Meat Bones, Braai Packs, Red Meats, Wors, Chicken Feets, Liver.'

order = input(name + ', what would you like to buy  in our menu today? Here is what we are serving.\n\n' + menu)

if order == "Liver":
    price = 300
elif order == "Red Meat":
    price = 320
elif order == "Chicken Feets":
    price = 150
elif order == "Meat bones":
    price = 270
elif order == "Braai Packs":
    price = 180
elif order == "Beef Sausages":
    price = 150
elif order == "Mnandi Mince Meat":
    price = 120
elif order == "Wors":
    price = 200
else:
    print("Sorry, we don't have that kind of meat here.")
    price = 0
    exit()

quantity = input('How many packets would you like?\n')

total = price * int(quantity)

print('Sounds good ' + name + ', we will have your ' + quantity + ' ' + order + ' packets ready for you in a moment.\n')
print('Thank you Sir/Madam. Your total is: R' + str(total))
#After giving the costumer the meat
print('Have a good day ' + name + ', and enjoy your meat.\n')

#If Consumer finds the meat rotten or expired!!
print('Good day Sir/Madam\n')

name = input("What is your name Sir/Madam?\n")

input("How can we help you today?\n")

receipt = input("Can we have your receipt to confirm that you bought this meat here at Zondi Butchery Store.\n")

if receipt == "NO Receipt":
    print("Sorry " + name + ", we cannot help you if you don't have the receipt. Have a good day!!")
    exit()
else:
    print("Sorry for what happened to your meat.\n")
input("Can we refund your money?\n")
price_EM = (input("How much was the meat you bought?\n"))

print("Here is your total: R" + str(price_EM) + " you used for the meat.\n Hope to hear from again " + name + ", Have a good day "  )

 
 



