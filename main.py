import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Load the dataset
df = pd.read_csv('RaceResults.csv')

# Load the background image
template = Image.open('bg.jpeg')

# Use the Caladea font
font_path = '/usr/share/fonts/google-crosextra-caladea-fonts/Caladea-Regular.ttf'
name_font = ImageFont.truetype(font_path, 50)
other_font = ImageFont.truetype(font_path, 30)

# Coordinates for the text placement
name_coords = (300, 200)
position_coords = (300, 300)
time_coords = (300, 400)

# Directory to save the certificates
output_dir = "certificates/"

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Create certificates for each participant
for index, row in df.iterrows():
    certificate = template.copy()
    draw = ImageDraw.Draw(certificate)

    draw.text(name_coords, row['NAME'], font=name_font, fill='black')
    draw.text(position_coords, f"Finish Position: {row['Finish Position']}", font=other_font, fill='black')
    draw.text(time_coords, f"Net Finish Time: {row['Net Finish Time']}", font=other_font, fill='black')

    certificate.save(f"{output_dir}{row['NAME']}_certificate.pdf", "PDF")

print("Certificates generated successfully!")
