time_slots = ["Dawn","Morning", "Midday", "Afternoon", "Evening","Dusk"]
heart_rates = []

for time in time_slots:
    hr = int(input(f"Please enter your heartrate (In BPM) in the {time} : "))
    heart_rates.append(hr)

print()

total_heart_rate = sum(heart_rates)
avg_heart_rate = total_heart_rate / len(time_slots)

print(f"Your average Heart Rate today is {avg_heart_rate}")
