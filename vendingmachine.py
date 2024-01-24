#list all items in vending machine and their prices and stocks
def vend():

    a = {'candy': 'lollipop', 'price': 1, 'stock': 11}
    b = {'candy': 'bubblegum', 'price': 2, 'stock': 12}
    c = {'candy': 'haribo', 'price': 3, 'stock': 13}
    d = {'candy': 'hersheys', 'price': 4, 'stock': 14}
    e = {'candy': 'sodapop', 'price': 5.20, 'stock': 15}
    f = {'candy': 'snickers', 'price': 6, 'stock': 13}
    g = {'candy': 'nerds', 'price': 10, 'stock': 14}
    h = {'candy': 'magicpop', 'price': 6.75, 'stock': 12}
    i = {'candy': 'skittles', 'price': 1, 'stock': 11}
    j = {'candy': 'candycane', 'price': 12, 'stock': 12}
    k = {'candy': 'maltesers', 'price': 8, 'stock': 13}
    l = {'candy': 'mars', 'price': 6, 'stock': 12}
    m = {'candy': 'sourpunk', 'price': 4.50, 'stock': 11}
    candies = [a, b, c, d, e, f, g, h, i, j, k, l, m]
    cim = 0 # cash in machine

    print('welcome to the candy machine! \n***************')

    # show candies, prices
    def show(candies):
        print('\ncandies available \n***************')

        for candy in candies:      
            if candy.get('stock') == 0:
                candies.remove(candy)
        for candy in candies:
            print(candy.get('candy'), candy.get('price'))

        print('***************\n')
    purchase = True
    # have user choose candy
    while purchase == True:
        show(candies)
        selected = input('select candy: ')
        for candy in candies:
            if selected == candy.get('candy'):
                selected = candy              
                price = selected.get('price')
                while cim < price:
                    cim = cim + float(input('insert ' + str(price - cim) + ': '))   

                print('you got ' + selected.get('candy'))
                selected['stock'] -= 1
                cim -= price
                print('cash remaining: ' + str(cim))
                a = input('do you wish to add more? (yes/no): ')
                if a == 'no': 
                    purchase = False 

                    if cim != 0:
                        print(str(cim) + ' refunded')
                        cim = 0
                        print('Alright then, enjoy your treat!\n')
                        break                        
                    else:
                        print('Alright then, enjoy your treat!\n')
                        break  
                else:
                    continue 
vend()               
