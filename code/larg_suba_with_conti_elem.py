
def findLength(arr, n):
      

    max_len = 1 
    for i in range(n - 1):
      

        mn = arr[i]
        mx = arr[i]
  

        for j in range(i + 1, n):
          

            mn = min(mn, arr[j])
            mx = max(mx, arr[j])
  

            if ((mx - mn) == j - i):
                max_len = max(max_len, mx - mn + 1)
          
    return max_len