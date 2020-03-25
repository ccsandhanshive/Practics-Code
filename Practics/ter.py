def delete(List1,List2):
    List1=set(List1)-set(List2)
    return List1

red_desk=(['R_1','R_2','R_3','R_4','R_5','R_6','R_7','R_8','R_9','R_Reverse','R_DrawTwo','R_Wild','R_WildDrawFour','R_Skip'])
yellow_desk=(['Y_1','Y_2','Y_3','Y_4','Y_5','Y_6','Y_7','Y_8','Y_9','Y_Reverse','Y_DrawTwo','Y_Wild','Y_WildDrawFour','Y_Skip'])
Green_desk=(['G_1','G_2','G_3','G_4','G_5','G_6','G_7','G_8','G_9','G_Reverse','G_DrawTwo','G_Wild','G_WildDrawFour','G_Skip'])
blue_desk=(['B_1','B_2','B_3','B_4','B_5','B_6','B_7','B_8','B_9','B_Reverse','B_DrawTwo','B_Wild','B_WildDrawFour','B_Skip'])

serv_cards=[]
final_desk= red_desk+yellow_desk+Green_desk+blue_desk
print(len(final_desk))
final_desk=delete(final_desk,red_desk)
print(len(final_desk))    