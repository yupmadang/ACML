"""
This Code Estimates Fuel Mass for Satellite Missions
Using the Rocket Equation.
"""

import math
import planetary_data as pd  # Planetary data module


def rocket_equation(delta_v, isp, dry_mass, height, center):
    """
    Calculate fuel mass required for a satellite using the rocket equation.
    
    Args:
        delta_v (float): Required velocity change (m/s).
        isp (float): Specific impulse (s).
        dry_mass (float): Dry mass of the satellite (kg).
        height (float): Orbital height above the planet's surface (km).
        center (str): Name of the central body ('Earth', 'Mars', etc.).
    
    Returns:
        float: Fuel mass required (kg).
    """
    # Convert center name to lowercase for uniformity
    center = center.lower()

    # Fetch planetary data dynamically
    planet_data = getattr(pd, center, None)
    if not planet_data:
        raise ValueError(f"Unknown planet: {center}")

    # Extract planetary parameters
    G = planet_data.get('mu')  # Gravitational parameter (km^3/s^2)
    R = planet_data.get('radius')  # Planet radius (km)

    if G is None or R is None:
        raise ValueError(f"Missing data for planet: {center}")

    # Calculate gravitational acceleration at the given height
    g_h = G / (R + height)**2

    # Calculate effective exhaust velocity
    v_e = isp * g_h  # Effective exhaust velocity (m/s)

    # Rocket equation to calculate fuel mass
    fuel_mass = dry_mass * (math.exp(delta_v / v_e) - 1)
    return fuel_mass


"""
if __name__ == "__main__":
    try:
        # Inputs
        delta_v = 2000  # m/s
        isp = 300  # seconds
        dry_mass = 407  # kg
        height = 150  # km above surface
        center = "Earth"  # Central body

        # Calculate fuel mass
        fuel_mass = rocket_equation(delta_v, isp, dry_mass, height, center)
        print(f"Fuel mass required: {fuel_mass:.2f} kg")

    except ValueError as e:
        print(f"Error: {e}")
"""