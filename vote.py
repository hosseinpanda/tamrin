print("lotfan etelaat ra vared konid")
name=input("naam va naam khanevadegi khod ra benevisid : ")
code=input("code melli khod ra vared konid : ")
bday=input("saal tavalod khod ra vared konid : ")
sen=1403-int(bday)
if sen>=18 :
	f=open("C:\\vote\\vote.txt","x")
	ray=input("pezeshkian ya Jalili? ")
	f.write(name)
	f.write(code)
	f.write(bday)
	f.write(ray)
	f.close()
else :
	f=open("C:\\vote\\vote.txt","x")
	prin=input("-100000 social credit")
	f.write(prin)
