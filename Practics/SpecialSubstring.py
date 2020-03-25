def func(string):
    start,end=0,0
    while start<len(string):
        if string[end]==string[end-start]:
            print(string[start:end+1],end=" ")
            end+=1
            if end==len(string):
                start+=1
                end=start
            else:
                start+=1
                end=start
func("chetan")