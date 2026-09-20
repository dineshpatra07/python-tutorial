age = 20
current_time_24_hr = 21

check_age=(age >=18)

check_current_time_condition=(current_time_24_hr >=18)and(current_time_24_hr <=23)

can_they_party=(check_age) and (check_current_time_condition)

print("allow in club!",can_they_party)