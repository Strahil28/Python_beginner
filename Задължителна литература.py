page_number_in_book = int(input("Enter page number in book: "))
read_page_from_hour = int(input("Enter how many page read per 1 hour: "))
day_read_current_book = int(input("Enter need days read current book: "))

need_time_read_book = page_number_in_book / read_page_from_hour
need_hour_per_days = need_time_read_book / day_read_current_book

print(int(need_hour_per_days))