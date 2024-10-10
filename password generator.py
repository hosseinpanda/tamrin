import random

x=int(input('lotfan tedad charecter ha ra benevisid : '))

sal = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bal = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','v','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']

randomsal = random.sample(sal,26)
randombal = random.sample(bal,26)
randomnum = random.sample(num,10)

ranpass = randomsal + randombal + randomnum

password = random.sample(ranpass,x)

final = "".join(password)

print("ramz obor shoma ("+final+ ") ast")
