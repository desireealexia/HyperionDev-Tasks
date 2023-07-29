# list of menu items in cafe
menu = ["tea", "coffee", "bagel", "croissant"]

# dictionary containing the stock value for each item on menu
stock = {"tea": 60, 
         "coffee": 75, 
         "bagel": 30, 
         "croissant": 25
        }

# dictionary containing prices for each item on menu
price = {"tea": 1.50, 
         "coffee": 2.00, 
         "bagel": 2.50, 
         "croissant": 2.30
        }

# calculate the total_stock worth in the cafe
total_stock = 0
for item in menu:
    total_stock += stock[item] * price[item]
print(total_stock)
