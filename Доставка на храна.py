chicken_menu = 10.35
fish_menu = 12.40
vegetable_menu = 8.15

number_chicken_menu = int(input("Enter number chicken menu: "))
number_fish_menu = int(input("Enter number fish menu: "))
number_vegetable_menu = int(input("Enter number vegetable menu: "))

price_chicken_menu = number_chicken_menu * chicken_menu
price_fish_menu = number_fish_menu * fish_menu
price_vegetable_menu = number_vegetable_menu * vegetable_menu

sum = price_chicken_menu + price_fish_menu + price_vegetable_menu
price_desert = sum * 0.20

need_sum = sum + price_desert + 2.50

print("Need sum: ", round(need_sum, 2))