import streamlit as st
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple line plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Set plot labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sinusoidal Curve')

# Save the plot as an image
image_path = "sinusoidal_plot.png"
fig.savefig(image_path)

# Display the image using st.image
st.image(image_path, use_column_width=True)

# Optionally, remove the saved image file
# import os
# os.remove(image_path)
