# 01_example_app.py
import streamlit as st

from functions.calculations import calculate_spiral
from components.spiral_chart import spiral_chart

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions,
checkout our [documentation](https://docs.streamlit.io)
and [community forums](https://discuss.streamlit.io).

In the meantime,
below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# calculate axises and indices
x, y, indices = calculate_spiral(num_points, num_turns)

# plot chart
spiral_chart(x, y, indices, num_points)
