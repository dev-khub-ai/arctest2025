import os
from PIL import Image

os.environ["DISPLAY"] = "localhost:0.0"  # Ensure X server is set
img = Image.open("grid_0_0.png")
img.show(command="feh")

