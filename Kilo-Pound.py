# This program is designed to convert Kilograms to Pounds
#Define variables for Kilogram vaules
kg_value_1 = 2.2
kg_value_2 = 5.4
kg_value_3 = 9
kg_value_4 = 13.6

# Conversion factor: 1kg = 2.20462lb's
conversion_factor = 2.204621  

# Calcuate lbs for each kg value
lb_1 = kg_value_1 * conversion_factor
lb_2 = kg_value_2 * conversion_factor
lb_3 = kg_value_3 * conversion_factor
lb_4 = kg_value_4 * conversion_factor

# Output the results
print(f"{kg_value_1} kilograms is equal to {lb_1:.2f} lbs")
print(f"{kg_value_2} kilograms is equal to {lb_2:.2f} lbs")
print(f"{kg_value_3} kilograms is equal to {lb_3:.2f} lbs")
print(f"{kg_value_4} kilograms is equal to {lb_4:.2f} lbs")