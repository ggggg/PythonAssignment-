print('enter currency, USD or CAD:')
currency = input().upper()
print('Enter value:')
value = float(input())
if (currency == 'USD'):
    print('The value in CAD is: $' + str(value * 1.27))
elif (currency == 'CAD'):
    print('The value in USD is: $' + str(value * 0.79))
else:
    print('Currency not found.')
