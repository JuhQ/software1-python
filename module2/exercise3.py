length = float(input("Give length: "))
width = input("Give width: ")
width = float(width)

perimeter = (length * 2) + (width * 2)
area = width * length

print(f"Perimeter: {perimeter}")
print(f"Perimeter: {(length * 2) + (width * 2)}")
print(f"Area: {area:.2f}")
print(f"Area: {area:<26.2f}")
print(f"Area: {area}")

print(f"Test: {area:.0f}")

print("Perimeter: " + str(perimeter))