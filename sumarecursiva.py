def sumatorio(m):
    if m > 0:
        return m + sumatorio(m-1)
    else:
        return 0
    
print(sumatorio(4))