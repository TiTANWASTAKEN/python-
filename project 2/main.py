import os
import shutil
import subprocess
import tkinter as tk

def divide_files(input_folder, output_folder_base, num_parts):
    for i in range(1, num_parts + 1):
        output_folder = os.path.join(output_folder_base, f'part_{i}')
        os.makedirs(output_folder, exist_ok=True)

    all_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    files_per_part = len(all_files) // num_parts

    for i in range(num_parts):
        start_index = i * files_per_part
        end_index = (i + 1) * files_per_part if i < num_parts - 1 else len(all_files)
        part_files = all_files[start_index:end_index]

        output_folder = os.path.join(output_folder_base, f'part_{i + 1}')
        for file in part_files:
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)
            shutil.move(input_path, output_path)

    return [os.path.join(output_folder_base, f'part_{i + 1}') for i in range(num_parts)]

def run_process(paths):
    folder_paths = divide_files(**paths)
    launch_application(folder_paths)

def launch_application(folder_paths):
    for i, folder_path in enumerate(folder_paths, start=1):
        application_path = r'C:\Path\To\Your\Application.exe'  # Replace with the actual path to your application
        subprocess.Popen([application_path, folder_path])
        print(f"Launched application for part_{i}")

# Create the main application window
app = tk.Tk()
app.title("File Division and Application Launcher")

# Define 9 sets of input and output folder paths
sets_of_paths = [
    {"input_folder": r'C:\Path\To\Set1\Input\Folder', "output_folder_base": r'C:\Path\To\Set1\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set2\Input\Folder', "output_folder_base": r'C:\Path\To\Set2\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set1\Input\Folder', "output_folder_base": r'C:\Path\To\Set1\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set2\Input\Folder', "output_folder_base": r'C:\Path\To\Set2\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set1\Input\Folder', "output_folder_base": r'C:\Path\To\Set1\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set2\Input\Folder', "output_folder_base": r'C:\Path\To\Set2\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set1\Input\Folder', "output_folder_base": r'C:\Path\To\Set1\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set2\Input\Folder', "output_folder_base": r'C:\Path\To\Set2\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set1\Input\Folder', "output_folder_base": r'C:\Path\To\Set1\Output\Base\Folder', "num_parts": 3},
    {"input_folder": r'C:\Path\To\Set2\Input\Folder', "output_folder_base": r'C:\Path\To\Set2\Output\Base\Folder', "num_parts": 3},
    
]

# Create and pack buttons for each set
for index, paths in enumerate(sets_of_paths, start=1):
    button_text = f"Run Process {index}"
    button_command = lambda paths=paths: run_process(paths)
    button = tk.Button(app, text=button_text, command=button_command)
    button.pack(pady=10)

# Start the GUI event loop
app.mainloop()

