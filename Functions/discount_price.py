
def discount_price(price):

    if price >= 300:
        price *= 0.7
    elif price >= 200 and price < 300:
        price *= 0.8
    elif price >= 100 and price < 200:
        price *= 0.9
    elif price >= 0 and price < 100:
        price *= 0.95

    return price

price = int(input("Enter the price: "))
print("$", discount_price(price))
