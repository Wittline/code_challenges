def SetZeroes(mat):

    M, N = len(mat), len(mat[0])
    fr, fc = False, False    

    for r in range(M):        
        if mat[r][0] == 0:
            fc = True
            break

    for c in range(N):
        if mat[0][c] == 0:
            fr = True
            break
    
    for r in range(1, M):
        for c in range(1, N):
            if mat[r][c] == 0:
                mat[0][c] = 0
                mat[r][0] = 0
    
    for r in range(1, M):
        if mat[r][0] == 0:
            for c in range(1, N):
                mat[r][c] = 0

    for c in range(1, N):
        if mat[0][c] == 0:
            for r in range(1, M):
                mat[r][c] = 0
    
    if fr:
        mat[0] = [0]*N
    if fc:
        for r in range(M):
            mat[r][0] = 0


                



# def SetZeroes(mat):

#     M, N = len(mat), len(mat[0])
#     row, col = [1]*M, [1]*N


#     for r in range(M):
#         for c in range(N):
#             if mat[r][c] == 0:
#                 row[r] = 0
#                 col[c] = 0
    
#     for r in range(M):
#         if row[r] == 0:
#             mat[r] = [0]* N
    
#     for c in range(N):
#         if col[c] == 0:
#             for r in range(M):
#                 mat[r][c] = 0




    
        


