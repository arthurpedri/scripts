import os

def rename_mp4_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter out only .mp4 files
    mp4_files = [f for f in files if f.endswith('.mp4')]
    
    # Sort the files alphabetically
    mp4_files.sort()
    # Rename files to incrementing numbers
    for index, filename in enumerate(mp4_files):
        new_name = f"{index + 1}.mp4"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} to {new_path}")

# Replace 'your_directory_path' with the path to your directory
directory_path = '/media/voga/HD/Pictures/Câmera/Vídeos/Viagem Europa/teste'
rename_mp4_files(directory_path)
