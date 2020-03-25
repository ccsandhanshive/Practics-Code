def transpose(the_array):
    res = []
    for i in range(len(the_array)):
        transposed = []
        for col in the_array:
            transposed.append(col[i])
        transposed.reverse()
        res.append(transposed)
    return res

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))