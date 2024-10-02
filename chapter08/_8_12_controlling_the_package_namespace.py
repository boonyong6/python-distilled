# Example:
# `graphics` is the top-level package namespace.
import graphics

# graphics.primitive.fill.flood_fill()  # Fails


# Example:
from graphics import Plot2D

plt = Plot2D(100, 100)
plt.clear()