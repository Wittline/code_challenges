def rotate(mat):

    l, r = 0, len(mat) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topleft = mat[top][l + i]
            mat[top][l + i] = mat[bottom - i][l]
            mat[bottom - i][l] = mat[bottom][r - i]
            mat[bottom][r - i] = mat[top + i][r]
            mat[top + i][r] = topleft        
        r -=1
        l +=1

if __name__ == "__main__":
    
    mat = [[1,2,3,4],[5,6,7, 8],[9,10,11, 12], [13,14,15, 16]]    
    rotate(mat)
    print(mat)


