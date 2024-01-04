def fibo(n):
    result = [0] * n
    if n != 1:
        result[1] = 1
        for i in range(2, n):
            result[i] = result[i-1] + result[i-2]

    return result


n = int(input("Enter a number: "))
print(fibo(n))