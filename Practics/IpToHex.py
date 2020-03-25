def returnHexValues(arg):
    val=int(arg)
    string=" "
    temp=val%16
    val=val/16
    
    if val==0:
        string=string+" "
    elif val<10:
        string=string+'%d'%(val)
    elif val==10:
        string=string+'A'
    elif val==11:
        string=string+'B'
    elif val==12:
        string=string+'C'
    elif val==13:
        string=string+'D'
    elif val==14:
        string=strimg+'E'
    elif val==15:
        string=string+'F'
        
    if temp==0:
        string=string+" "
    elif temp<10:
        string=string+'%d'%(temp)
    elif temp==10:
        string=string+'A'
    elif temp==11:
        string=string+'B'
    elif temp==12:
        string=string+'C'
    elif temp==13:
        string=string+'D'
    elif temp==14:
        string=string+'E'
    elif temp==15:
        string=string+'F'
    
    return string
splittedAddress=[]
address=input("Enter ip address:")
splittedAddress=address.split('.')
Address=" "

for i in splittedAddress:
    Address+=returnHexValues(i)

print(Address)