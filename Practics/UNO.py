import random


def Order(player,n,order,i):
    while True:
        print("player{}->{}".format(i,player[i]))
        card_number=int(input("Enter card no to serve"))
        if len(serv_cards)==0 or checkMatchning(player[i][card_number],serv_cards[len(serv_cards)-1],player,n,order,i,card_number):
            serv_cards.append(player[i][card_number])
            print(serv_cards)
            player[i].remove(player[i][card_number])
        else:
            print("invalid")
            print(serv_cards)
            player[i].append(random.choice(final_desk))
        
        if order==0 or order==10:
            if i>=n-1:
                i=0
            else:
                i=i+1
        elif order==1:
            if i<=0:
                i=n-1
            else:
                i=i-1
                        
            

def checkMatchning(card1,card2,player,n,order,i,card_number):
    res1=card1.split('_')
    res2=card2.split('_')
    if res1 == res2:
        return True
    elif res1[0]==res2[0]:
        checkAction(res1,order,i,player,n,card_number)
        return True
    elif res1[1]==res2[1]:
        checkAction(res1,order,i,player,n,card_number)
        return True
    else:
        return False

def drawTwo(player,i,n):
    if i>=n-1:
        player[0].append(random.choice(final_desk))
        player[0].append(random.choice(final_desk))
    else:
        player[i].append(random.choice(final_desk))
        player[i].append(random.choice(final_desk))
        
def wild(i,card_number):
    print("choose color:")
    print("     R->RED")
    print("     Y->YELLOW")
    print("     G->GREEN")
    print("     B->.BLUE")
    color=input("Enter color")
    player[i][card_number]='{}_wild'.format(color)

def checkAction(res1,order,i,player,n,card_number):
    if res1[1]=="Reverse" and (order==0 or order==10):
        if i==0:
            Order(player,n,1,n)
        else:
            Order(player,n,1,i-1)
    elif res1[1]=="Reverse" and order==1:
        if i==n:
            Order(player,n,0,0)
        else:
            Order(player,n,1,i+1)
        
    elif res1[1]=="DrawTwo" and (order==0 or order==10):
        drawTwo(player,i+1,n)
    elif res1[1]=="DrawTwo" and order==1:
        drawTwo(player,i-1,n)
    elif res1[1]=="Wild":
        res1[0]=wild(i,card_number)
    elif res1[1]=="WildDrawFour":
        
        if order==0 or order==10:
            drawTwo(player,i+1,n)
            drawTwo(player,i+1,n)
        if order==1:
            drawTwo(player,i-1,n)
            drawTwo(player,i-1,n)
    elif res1[1]=="Skip":
        if i==0 and (order==0 or order==10): 
            Order(player,n,order,i+2)
        elif i==n and order==1:
            Order(player,n,order,n-2)
        elif i==n and (order==0 or order==10):
            Order(player,n,order,1)
        elif order==0 or order==10:
            Order(player,n,order,i+2)
        else :
            Order(player,n,order,i-2)
    return res1[0]

    
    
    
    
    
red_desk=['R_1','R_2','R_3','R_4','R_5','R_6','R_7','R_8','R_9','R_Reverse','R_DrawTwo','R_Wild','R_WildDrawFour','R_Skip']
yellow_desk=['Y_1','Y_2','Y_3','Y_4','Y_5','Y_6','Y_7','Y_8','Y_9','Y_Reverse','Y_DrawTwo','Y_Wild','Y_WildDrawFour','Y_Skip']
Green_desk=['G_1','G_2','G_3','G_4','G_5','G_6','G_7','G_8','G_9','G_Reverse','G_DrawTwo','G_Wild','G_WildDrawFour','G_Skip']
blue_desk=['B_1','B_2','B_3','B_4','B_5','B_6','B_7','B_8','B_9','B_Reverse','B_DrawTwo','B_Wild','B_WildDrawFour','B_Skip']

serv_cards=[]
final_desk= red_desk+yellow_desk+Green_desk+blue_desk
n=int(input("Enter no of player"))
no_of_cards=int(input("enter initial number of cards"))
player=[]
for i in range(0,n):
    sample=random.sample(final_desk,no_of_cards)
    player.append(sample) 

Order(player,n,10,0)
    

    