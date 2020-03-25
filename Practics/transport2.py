def transeport(array):
    res=[]
    for i in range(len(array)):
        transport=[]
        for j in array:
            transport.append(j[i])
        transport.reverse()
        res.append(transport)
    return res
print(transeport([[1,2,3],[4,5,6],[7,8,9]]))