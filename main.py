def array_int(arr):
    result=[]
    for n in arr:
        if n == 0:
            result.append(0)
            continue
        product=1
        while n:
            digit= abs(n)%10
            product*= digit if digit != 0 else 1
            n//=10
        result.append(product)
    return result
arr= [26,54,32 ]
print(array_int(arr))


