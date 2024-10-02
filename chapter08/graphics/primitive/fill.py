# Run this module under the chapter08 directory:
#   chapter08$ py -m graphics.primitives.fill

# # Fully qualified submodule import
# from graphics.primitives import lines

# Package-relative import
from . import lines

def flood_fill():
    ...

print(f"Imported {__name__}")
