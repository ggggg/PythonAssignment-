# get currency
print('enter currency, USD or CAD:')
currency = input().upper()
# get the value
print('Enter value:')
value = float(input())
# usd
if (currency == 'USD'):
  # make calculation and output result
    print('The value in CAD is: $' + str(value * 1.27))
# cad
elif (currency == 'CAD'):
  # make calculation and output result
    print('The value in USD is: $' + str(value * 0.79))
# currency not found
else:
    print('Currency not found.')
