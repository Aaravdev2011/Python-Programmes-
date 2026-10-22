#Part    - Types of data
snack_name = "chips"  # str - text
price = 1.50  # float - decimal
quanitity = 10  # int - whole number
is_available = True  # bool - True or False

print("Snack:" , snack_name)
print("Price: $" , price)
print("In stock:" , quanitity)
print("available?", is_available)

print ( type(snack_name) )
print ( type(price) )
print ( type(quanitity) )
print ( type(is_available) )

# Part 2 - Arithmetic operators 
total = price * quanitity
print("Total value : $" , total )
print("Sale price: $" , price - 0.25)
print("double stock: " , quanitity * 2)

#Part 3 - comparaison operators
print("IS price under $2?" , price < 2)
print("More than 5 in stock?" , quanitity > 5)
print("Is price exactly $1.50" , price == 1.50)

# PART 4 -  STRING OPERATORS
shop_name = "Quick" + "" + "Bites"
print("shop name:" , shop_name)
print("Letters in snack name:" , len(snack_name))
print ("First letter:" , snack_name[0])

#PART 5 - Swapping Values

price_a = 1.50
price_b = 3.00
print("before:" , price_a , "and" , price_b) 

temp = price_a
price_a = price_b
price_b = temp

print("After:" , price_a , "and", price_b)