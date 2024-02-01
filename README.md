markdown
Copy code
# Offline Flask File List Display

This Flask application displays the names of files in two folders on an offline computer. The file list is presented on a webpage with an airport-style interface, including a progress bar to visualize the completion percentage of files in Folder 2.

## Setup Instructions

### 1. Download Flask and Dependencies

On an online computer with internet access:

```bash
pip download Flask
Transfer the downloaded wheel files to the offline computer.

2. Install Flask and Dependencies
On the offline computer:

bash
Copy code
pip install path\to\flask-3.0.1-py3-none-any.whl
pip install path\to\blinker-1.7.0-py3-none-any.whl
pip install path\to\click-8.1.7-py3-none-any.whl
pip install path\to\itsdangerous-2.1.2-py3-none-any.whl
pip install path\to\jinja2-3.1.3-py3-none-any.whl
pip install path\to\werkzeug-3.0.1-py3-none-any.whl
pip install path\to\markupsafe-2.1.4-cp310-cp310-win_amd64.whl
pip install path\to\colorama-0.4.6-py2.py3-none-any.whl
3. Clone the Repository
Clone this repository on the offline computer.

bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
4. Run the Flask Application
bash
Copy code
python your_flask_app.py
This will start the Flask application. Open a web browser and navigate to http://127.0.0.1:5000/ to view the file lists and the progress bar.

5. Customize Folder Paths
Edit the Flask application (your_flask_app.py) to set the correct paths for folder1_path and folder2_path based on your file structure.

Notes
Ensure that Python and pip are installed on the offline computer.
Adjust file paths, folder names, and repository details as needed.
