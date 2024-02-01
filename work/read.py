import os
from flask import Flask, render_template

app = Flask(__name__)

def list_files(folder_path):
    try:
        files = os.listdir(folder_path)
        return files
    except OSError as e:
        print(f"Error reading files from {folder_path}: {e}")
        return []

@app.route('/')
def display_files():
    folder1_path = r"C:\Users\rithi\Desktop\result"
    folder2_path = r"C:\Users\rithi\Desktop\bug"

    files_folder1 = list_files(folder1_path)
    files_folder2 = list_files(folder2_path)

    return render_template('index.html', files_folder1=files_folder1, files_folder2=files_folder2)

if __name__ == '__main__':
    app.run(debug=True)

