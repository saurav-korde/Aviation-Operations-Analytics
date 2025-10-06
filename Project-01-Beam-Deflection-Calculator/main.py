# A simple calculator for beam deflection

print("Beam Deflection Calculator")

# We will assume some values for the beam's material and shape
# E is for the material (Aluminum)
e_modulus = 69000000000.0
# I is for the cross-section shape (2x4cm rectangle)
i_moment = 0.00000001067

# Get the details from the user
force = float(input("Enter the force in Newtons: "))
length = float(input("Enter the beam length in meters: "))

# Calculate the deflection using the formula
# deflection = (force * length^3) / (3 * E * I)
numerator = force * (length ** 3)
denominator = 3 * e_modulus * i_moment
deflection_in_meters = numerator / denominator

# Convert the result to millimeters to make it easier to read
deflection_in_mm = deflection_in_meters * 1000

# Print the final result
print("The deflection at the end of the beam is:")
print(deflection_in_mm)
