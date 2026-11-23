shopping_list = ["milk", "bread", "eggs", "apples"]
prices = [2.5, 1.5, 3.0, 4.0]
total_cost = sum(prices)
shopping_list.append("cheese")
prices.append(5.0)
shopping_list.remove("bread")
prices.remove(1.5)
shopping_list[3] = "chocolate"
prices[3] = 6.0
total_items = len(shopping_list)
print(shopping_list)
print(prices)
print("Total cost of the shopping list:", total_cost)
print(shopping_list[1:-1])
print("Total items in the shopping list:", total_items)
