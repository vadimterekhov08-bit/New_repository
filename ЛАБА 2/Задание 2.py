def describe_person(name, age = 30):
    print(f'Человеку по имени {name} {age} лет')

name = str(input())
age = input()
if age:
    describe_person(name, age)
else:
    describe_person(name)