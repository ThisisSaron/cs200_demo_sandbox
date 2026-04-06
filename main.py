def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    y = int(input('num:'))
    while y != 0:
        lst.append(y)
        y = int(input('num:'))
    print('You added', len(lst), 'numbers')
    return lst


def foo(x,y):
    return (x*y) + 1


def bar(z):
    return (z%2) == 0 

def func2(data):
    print('Here is the data:')
    print(data)

    selection = ''
    while True:
        selection = input('Select an option. 1-sum  2-min  3-max  4-quit')
        if selection == '1':
            print('The sum is', sum(data))
        elif selection == '2':
            print('Not supported yet')
        elif selection == '3':
            print('Not supported yet')
        elif selection == '4':
            print('Goodbye')
            return


def main():
    print("Hello, World!")
    data = func1()
    func2(data)

# ADDING A COMMENT


if __name__ == "__main__":
    main()
