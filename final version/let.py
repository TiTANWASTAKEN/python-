from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

def get_files_in_folder(folder_path, extensions):
    files = []
    for root, dirs, files_in_dir in os.walk(folder_path):
        for file in files_in_dir:
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                files.append(os.path.join(root, file))
    return files

def create_file_list(folder1_path, folder2_path, extensions):
    files_folder1 = get_files_in_folder(folder1_path, extensions)
    files_folder2 = get_files_in_folder(folder2_path, extensions)

    print(f"Files in {folder1_path}: {files_folder1}")
    print(f"Files in {folder2_path}: {files_folder2}")

    file_list = []
    for file_path in files_folder1:
        base, extension = os.path.splitext(os.path.basename(file_path))
        matching_files = [f for f in files_folder2 if os.path.splitext(os.path.basename(f).lower())[0] == base.lower()]

        if matching_files:
            is_different_extension = any(os.path.splitext(os.path.basename(f))[1].lower() != extension.lower() for f in matching_files)
            if is_different_extension:
                file_list.append({'name': os.path.basename(file_path), 'color': 'green'})
            else:
                file_list.append({'name': os.path.basename(file_path), 'color': 'red'})
        else:
            file_list.append({'name': os.path.basename(file_path), 'color': 'red'})

    # Sort the file_list based on color, prioritizing 'green'
    file_list.sort(key=lambda x: x['color'] == 'green', reverse=True)

    return file_list

@app.route('/screen1')
def screen1():
    folder1_path = r"D:\version 2\t1"
    folder2_path = r"D:\version 2\t2"
    extensions = ['.docx', '.pptx', '.xlsx']  # Add your desired extensions here

    file_list = create_file_list(folder1_path, folder2_path, extensions)

    current_month = datetime.now().strftime('%B %d')  # Format it as needed
    current_date = datetime.now().strftime('%m-%d-%Y')  # Format it as needed

    return render_template('screen1.html', file_list=file_list, current_month=current_month, current_date=current_date)

@app.route('/screen2')
def screen2():
    folder1_path = r"C:\Users\rithi\Desktop\work\version 3\t3"
    folder2_path = r"C:\Users\rithi\Desktop\work\version 3\t4"
    extensions = ['.docx', '.pptx', '.xlsx']  # Add your desired extensions here

    file_list = create_file_list(folder1_path, folder2_path, extensions)

    current_month = datetime.now().strftime('%B %d')  # Format it as needed
    current_date = datetime.now().strftime('%m-%d-%Y')  # Format it as needed

    return render_template('screen2.html', file_list=file_list, current_month=current_month, current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True)

