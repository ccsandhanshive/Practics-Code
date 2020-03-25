import datetime
flag=0
day=input()
days=["sunday","monday","thuesday","wednsday","thuesday","friday","saturday"]

if day not in days:
    print("invalid day")
    flag=1
    #exit()
if flag is 0:
    date1=input().split("/")
    try:
        datetime.datetime(int(date1[2]),int(date1[1]),int(date1[0]))
    except:
        print("invalid date")
        flag=1
     #   exit()
if flag is 0:
    noOfDay=days.index(day)
    #print("i= {}".format(noOfDay))       
    d0 = datetime.date(int("0001"),int("01"),int("01"))
    d1 = datetime.date(int(date1[2]),int(date1[1]),int(date1[0]))
    delta = d1 - d0
    #print("delta days={}".format(delta.days))
    
    Ofday = datetime.datetime(int("0001"),int("01"),int("01"))
    #print("Of day {}".format(Ofday.weekday()))
    diffDay=noOfDay-Ofday.weekday()
    #print("diff day {}".format(diffDay))
    Nfday=datetime.datetime(int(date1[2]),int(date1[1]),int(date1[0]))
    Nfday=Nfday.weekday()+diffDay  # what I look for
    #print("now day {}".format(Nfday))
    if (delta.days+diffDay%4 is 0 )or(Nfday is 6 or 0) :
        print("0")
    else:
        print(date1[0])