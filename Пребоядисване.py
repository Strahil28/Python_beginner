protective_nylon_price_meter = 1.50
paint_price_liter = 14.50
paint_thinner_price_liter = 5.00

need_meters_protective_nylon = int(input("Enter need protective nylon meters: "))
need_liters_paint = int(input("Enter need paint liters: "))
need_liters_paint_thinner = int(input("Enter need paint thinner liters: "))
work_hour = int(input("Enter need works hours: "))

nylon_sum = (need_meters_protective_nylon + 2) * protective_nylon_price_meter
paint_sum = (need_liters_paint + (need_liters_paint * 10 / 100)) * paint_price_liter
paint_thinner_sum = need_liters_paint_thinner * paint_thinner_price_liter

sum = nylon_sum + paint_sum + paint_thinner_sum + 0.40
works_man_sum = (sum * 30 / 100) * work_hour
need_sum = sum + works_man_sum

print(need_sum)