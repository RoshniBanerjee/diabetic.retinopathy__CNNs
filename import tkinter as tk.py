import tkinter as tk
from PIL import ImageTk, Image

# Create the main window
root = tk.Tk()
root.title("Background Image Example")

# Load the image
image_path = "D:/ROSHNI/SRM/2nd yr/4th srm/DIP/raw image.PNG"
img = Image.open(image_path)
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(img)

# Create a Canvas
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill=tk.BOTH, expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, image=background_image, anchor=tk.NW)

# Add other widgets or functionality here

# Run the GUI main loop
root.mainloop()
