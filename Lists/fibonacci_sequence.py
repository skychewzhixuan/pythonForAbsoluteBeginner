u = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 60, 987, 1597, 2584, 4181]

isFibonacciSequence = True
wrongIndex = 0

if u[0] != 0 or u[1] != 1:
    isFibonacciSequence = False

for index in range(2, len(u)):
        if u[index] != u[index-2] + u[index-1]:
            wrongIndex = index
            isFibonacciSequence = False
            break

if isFibonacciSequence:
    print('Hurrah ... we''ve got a Fibonacci list.')
else:
    print('It''s not a Fibonacci sequence due to the value', u[wrongIndex] ,'at index', wrongIndex, '.')