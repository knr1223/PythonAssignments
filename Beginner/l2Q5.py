# Function to analyze temperature data
def analyze_weather(temperature_readings):
    # Calculate average temperature
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    
    # Find the highest and lowest temperatures
    highest_temp = max(temperature_readings)
    lowest_temp = min(temperature_readings)
    
    # Return the results
    return avg_temp, highest_temp, lowest_temp

# Input: temperature readings
temperature_readings = list(map(int, input("Enter temperature readings (comma separated): ").split(',')))

# Call the function and get the results
avg_temp, highest_temp, lowest_temp = analyze_weather(temperature_readings)

# Output the results
print(f"Average Temperature: {avg_temp}")
print(f"Highest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")