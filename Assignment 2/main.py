#AC50002 - Programming languages for Data Engineering: 
# Python Assignment 2 - Euan Robertson: 2463967

import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Read in data from the CSV
data = pd.read_csv("GrowLocations.csv")

# Define the boundaries of the map (as stated in the brief)
lonMin, lonMax = -10.592, 1.6848
latMin, latMax = 50.681, 57.985

# Correct swapped Latitude and Longitude columns
data.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'},inplace=True)

# Remove values outside boundaries
data = data[data['Latitude'].between(latMin, latMax)]
data = data[data['Longitude'].between(lonMin, lonMax)]

# Remove duplicate values
data = data.drop_duplicates(subset=['Latitude', 'Longitude'])

# Load in the map
ukMap = Image.open("map7.png")

# Set map boundaries
mapBoundary = [lonMin, lonMax, latMin, latMax]

# Plot the data
plt.figure(figsize=(10, 8))

# Display the map as the background
plt.imshow(ukMap, extent=mapBoundary, aspect='auto', zorder=0)

# Plot the sensor locations
plt.scatter(
    data['Longitude'], data['Latitude'], 
    color='red', s=10, label="Sensor Locations", zorder=1
)

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Sensor Locations on UK Map")
plt.legend()

# Show the plot
plt.show()
