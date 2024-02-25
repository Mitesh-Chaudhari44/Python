temperatures = []
num_temperatures = int(input("Enter the number of temperatures: "))

for i in range(num_temperatures):
    temp = float(input(f"Enter temperature {i + 1}: "))
    temperatures.append(temp)

average_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)

total_temp = sum(temperatures)

print("Temperatures:", temperatures)
print("Average Temperature:", average_temp)
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
print("Total Temperature:", total_temp)
