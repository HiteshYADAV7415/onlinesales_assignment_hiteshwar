def compute(n):
    if n < 10:
        return n ** 2
    
    # n should be grester than 10 and less than 20
    elif n >= 10 and n <= 20: 
        fact = 1
    # loop should run from 1 to n-9    
        for i in range(1, n - 9):   
            fact *= i
        return fact
    elif n > 20:
        total = 0
     # Also for sum calculation loop should run from 1 to n-19   
        for i in range(1, n - 19):
            total += i
        return total

# Test cases
print(compute(1))  

