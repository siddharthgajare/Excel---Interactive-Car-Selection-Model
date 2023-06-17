# Intro line
print('\nWeclome to my exchange converter \nThis program is made by Siddharth Gajare\n\n')
# used input to assign value to usd
while True:
 usd=input("Tell me, How many amount of US dollars you want to exchange?")
     if usd.isdigit()==True:
        print(usd)
    else:
        print('Please add a numerical value of the usd')
        continue
    #used input to assign value to currency
currency = input('Tell me, Which currency do you want your money changed to?')
    if currency.isdigit()==False:
        print(currency)
    else:
        print('Please add a the alphabetical name for the currency,Thank you')
        continue
    Result = (float(usd) * float(exchange_rate))

    print (f'\nAfter converting USD to {currency} \nAmount you will receive : {Result} {currency}.\nThank you')
    break