rf_data = []
for i in range(12):
    rf = float(input(f"Enter the rainfall amount for month {i+1}: "))
    rf_data.append(rf)
total_rf = sum(rf_data)
average_rf = total_rf / len(rf_data)
max_index = rf_data.index(max(rf_data))
min_index = rf_data.index(min(rf_data))
max_month = max(rf_data)
min_month = min(rf_data)

print("Total Rainfall:", total_rf)
print("Average Rainfall:", average_rf)
print("Maximum Rainfall in a Month:", max_month, "at month:", max_index+1)
print("Minimum Rainfall in a Month:", min_month, "at month:", min_index+1)


