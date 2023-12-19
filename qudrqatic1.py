# Quadratic equation
temperature = 20.0
pressure = 800.0
humidity = 79.0

# Quadratic equation coefficients
a = 0.01
b = -0.5
c = 25

# Calculate weather parameter (e.g., precipitation)
precipitation = a * temperature**2 + b * humidity + c

# Print result
print(f"Precipitation: {precipitation}")
