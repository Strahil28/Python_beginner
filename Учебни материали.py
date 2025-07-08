pens_package_price = 5.80
markers_package_price = 7.20
preparation_price_per_liters = 1.20

number_pens_package = int(input("Enter number pens package: "))
number_markers_package = int(input("Enter number markers package: "))
liters_preparation = int(input("Enter preparation liters: "))
discount_percent = int(input("Enter discount percent: "))

sum_pens = number_pens_package * pens_package_price
sum_markers = number_markers_package * markers_package_price
sum_preparation = liters_preparation * preparation_price_per_liters
sum = sum_pens + sum_markers + sum_preparation

need_sum = sum - (sum * discount_percent / 100)

print(round(need_sum, 2))