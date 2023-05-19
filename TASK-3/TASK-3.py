def compute(n):
    if n < 10:
        out = n ** 2
     # 2-nd elseif condition has been changed and no it is runnig between 10 and 20   
    elif n >= 10 and n < 20:
        out = 1
     # Loop has been changed and now runnig from (1,n-10+1)  
        for i in range(1, n - 10 + 1):
            out *= i
    else:
        lim = n - 20
        # calculating the output using sum fuction in the range from 1, lim+1
        out = sum(range(1, lim + 1))
    return out

n = int(input("Enter an integer: "))
result = compute(n)
print(result)