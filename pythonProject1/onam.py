def print_flower(radius):
    for i in range(radius, -radius - 1, -1):
        for j in range(-radius, radius + 1):
            if i * i + j * j <= radius * radius:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

radius = 5  # Adjust the radius of the flower
print_flower(radius)
def print_round_shape(radius):
    for i in range(2 * radius + 1):
        for j in range(2 * radius + 1):
            distance = (i - radius)**2 + (j - radius)**2
            if distance <= radius**2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

radius = 5  # Adjust the radius of the round shape
print_round_shape(radius)

