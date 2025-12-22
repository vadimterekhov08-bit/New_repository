def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else: 
        return 'Халепа'
    

print(max_of_two(int(input('Первое число: ')), int(input('Второе число: '))))