from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_checkboxes = request.form.getlist('checkboxes[]')
        # Process the selected checkboxes as needed
        # ...

        return render_template('test_result.html', selected_checkboxes=selected_checkboxes)

    return render_template('test_index.html')

if __name__ == '__main__':
    app.run(debug=True)
