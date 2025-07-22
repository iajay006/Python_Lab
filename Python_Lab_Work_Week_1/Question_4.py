#Question 4 :

distance_km = 10
time_minutes = 43
time_seconds = 30

# Convert total time into hours
total_time_hours = (time_minutes + time_seconds / 60) / 60

# Convert kilometers to miles
distance_miles = distance_km / 1.61

# Average speed (miles/hour)
average_speed = distance_miles / total_time_hours

# Average time per mile
average_time_per_mile = total_time_hours / distance_miles * 60  # in minutes

print("Average speed (miles/hour):", round(average_speed, 2))
print("Average time per mile (minutes):", round(average_time_per_mile, 2))
