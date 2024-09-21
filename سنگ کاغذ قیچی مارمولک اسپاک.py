#sang gheychi va marmolak ro mizane . kaghaz sang va spock ro mizane . gheichi kaghaz va marmolak ro mizane . spock gheychi va sang ro mizane . marmolak spock va kaghaz ro mizane.


import random
print("salam be sang kaghaz gheychi marmolak spock khosh amadid")
possible_Action=['sang','kaghaz','gheychi','marmolak','spock']
human_selection=input('lotfan yek gozine az bein , sang , kaghaz , gheychi , marmolak va spock entekhab konid : ')
computer_selection=random.choice(possible_Action)
print(computer_selection)

if computer_selection==human_selection : 
    print("mosavi!!!")
    
    
if computer_selection=='sang' :
    if human_selection=='kaghaz' :
        print("ensan barande shod")

if computer_selection=='sang' :
    if human_selection=='gheychi' :
        print("cpu barande shod")

if computer_selection=='sang' :
    if human_selection=='marmolak' :
        print("marmolak leh shod(cpu barande shod)")

if computer_selection=='sang' :
    if human_selection=='spock' :
        print("ensan barande shod")
        
if computer_selection=='kaghaz' :
    if human_selection=='sang' :
        print("cpu barande shod")
        
if computer_selection=='kaghaz' :
    if human_selection=='gheychi' :
        print("ensan barande shod")
        
if computer_selection=='kaghaz' :
    if human_selection=='marmolak' :
        print("ensan barande shod")
        
if computer_selection=='kaghaz' :
    if human_selection=='spock' :
        print("cpu barande shod")
        
if computer_selection=='gheychi' :
    if human_selection=='sang' :
        print("ensan barande shod")
        
if computer_selection=='gheychi' :
    if human_selection=='kaghaz' :
        print("cpu barande shod")
        
if computer_selection=='gheychi' :
    if human_selection=='marmolak' :
        print("cpu barande shod")
        
if computer_selection=='gheychi' :
    if human_selection=='spock' :
        print("ensan barande shod") 
        
if computer_selection=='marmolak' :
    if human_selection=='sang' :
        print("marmolak leh shod(ensan barande shod)")
        
if computer_selection=='marmolak' :
    if human_selection=='kaghaz' :
        print("cpu barande shod")
        
if computer_selection=='marmolak' :
    if human_selection=='gheychi' :
        print("ensan barande shod")
        
if computer_selection=='marmolak' :
    if human_selection=='spock' :
        print("cpu barande shod")
        
if computer_selection=='spock' :
    if human_selection=='sang' :
        print("cpu barande shod")
        
if computer_selection=='spock' :
    if human_selection=='kaghaz' :
        print("ensan barande shod")
        
if computer_selection=='spock' :
    if human_selection=='gheychi' :
        print("cpu barande shod")
        
if computer_selection=='spock' :
    if human_selection=='marmolak' :
        print("ensan barande shod")