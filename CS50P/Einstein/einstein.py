def calculate_energy(mass):
    """
    Calculate the energy equivalent of the given mass using a simplified version of Einstein's E=mc^2 formula.

    Parameters:
    mass (int): Mass in kilograms.

    Returns:
    int: Energy in Joules.
    """
    # Simplified speed of light for the desired precision
    speed_of_light = 3e8  # 300,000,000 m/s
    energy = mass * speed_of_light ** 2
    return int(energy)

def main():
    """
    Prompt the user for mass and output the equivalent number of Joules.
    """
    mass = int(input("Enter mass in kilograms: "))  # User input for mass
    energy = calculate_energy(mass)  # Calculate the equivalent energy
    print(f"Equivalent energy in Joules: {energy}")

if __name__ == "__main__":
    main()
