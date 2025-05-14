import os

# Path to the folder containing your PNG files
folder_path = 'D:\Documents (D)\RPGs\Modern&Scifi\Traveller\Leaflet Map for Traveller\maps'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a PNG file
    if filename.endswith('.png'):
        # Find the position of 'UWP' and slice the string
        if 'UWP' in filename:
            new_name = filename.split(' UWP')[0] + '.png'  # Keep the part before ' UWP'
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_name}')
