import streamlit as st
import matplotlib.pyplot as plt
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

# Display the plot using st.pyplot
st.pyplot(fig)
