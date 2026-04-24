price = int(input("Enter price: "))
discount = int(input("Enter discount(%): "))
total = price * discount / 100
final_price = price - total
print("Price with discount: ", final_price)