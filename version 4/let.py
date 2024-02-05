from flask import Flask, render_template
import os

app = Flask(__name__)

def get_files_in_folder(folder_path):
    files = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            files.append(file)
    return files

def create_file_list(folder1_path, folder2_path):
    files_folder1 = get_files_in_folder(folder1_path)
    files_folder2 = get_files_in_folder(folder2_path)

    print(f"Files in {folder1_path}: {files_folder1}")
    print(f"Files in {folder2_path}: {files_folder2}")

    file_list = []
    for file in files_folder1:
        base, extension = os.path.splitext(file)
        matching_files = [f for f in files_folder2 if os.path.splitext(f.lower())[0] == base.lower()]

        if matching_files:
            is_different_extension = any(os.path.splitext(f)[1].lower() != extension.lower() for f in matching_files)
            if is_different_extension:
                file_list.append({'name': file, 'color': 'green'})
            else:
                file_list.append({'name': file, 'color': 'red'})
        else:
            file_list.append({'name': file, 'color': 'red'})

    return file_list

@app.route('/screen1')
def screen1():
    folder1_path = r"D:\version 2\t1"
    folder2_path = r"D:\version 2\t2"

    file_list = create_file_list(folder1_path, folder2_path)

    return render_template('screen1.html', file_list=file_list)

@app.route('/screen2')
def screen2():
    folder1_path = r"C:\Users\rithi\Desktop\work\version 3\t3"
    folder2_path = r"C:\Users\rithi\Desktop\work\version 3\t4"

    file_list = create_file_list(folder1_path, folder2_path)

    return render_template('screen2.html', file_list=file_list)

if __name__ == '__main__':
    app.run(debug=True)
