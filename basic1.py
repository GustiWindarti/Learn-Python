import math

def main():
    print('Hello world!')
    print('=====================')
    print('This is me.')
    print('You\'re looking for.')
    print('I can see it in your eyes.')
    print('I can see it in your smile.')
    print('You\'re all i ever wanted.')
    print('And my arms are open wide.')

    price=12.30
    print(price * math.pi)
    a=2
    b=3
    c=addStuff(a, b)
    print(c)
    
    print(2 * 3)

    uselessprice=1209312312.12

    price1 = 12.6
    price2 = 100.56
    result = addStuff(price1, price2)
    print(result)
    str_one = 'Gusti'
    str_two = 'Hello'
    str_three = addStuff(str_one, str_two)
    print(str_three)
    print(addStuff(str_one, price1))


def addStuff(a, b):
    c=a+b
    return c


if __name__ == "__main__":
    main()
