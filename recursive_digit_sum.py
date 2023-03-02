def superDigit(n, k):
    
    if len(n) == 1:
        return n
    else:
        
        total=0
        for num in n:
            total += int(num)
        total = str(total * k)

        return superDigit(total,1)
        
    return superDigit(n,1)
