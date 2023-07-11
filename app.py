from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        directory_path = request.form.get('directory_path')
        # Validate and process the directory_path as needed
        # ...

        # Check if the directory exists
        if not os.path.exists(directory_path):
            return render_template('index.html', error_message='Directory does not exist!')

        # Get a list of all files in the directory
        file_list = os.listdir(directory_path)

        # Filter only Excel files
        excel_files = []
        for file in file_list:
            if file.endswith('.xlsx') or file.endswith('.xls'):
                excel_files.append(file)

        # Display the available file names
        return render_template('page_two.html', excel_files=excel_files)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
