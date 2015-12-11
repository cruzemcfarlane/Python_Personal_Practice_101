def nthTri(n):
    def helper(total,y):
        if y==1:
            return total

        else:
            return helper(total+y,y-1)
    return helper(1,n)
