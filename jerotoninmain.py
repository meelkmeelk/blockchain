from flask import Flask, render_template, request
from data import *

app = Flask(__name__)

# Define a function to read the data from the text file and append the variables to a Python file
def read_data():
    with open('data.txt', 'r') as file:
        # Read the file and split it into rows
        file_content = file.read()
        rows = file_content.split('\n')
        
        # Create a list of variables, where each variable corresponds to a row of data
        var_names = [f't{i+1}' for i in range(len(rows))]
        var_values = [f'"{row}"' for row in rows]
        var_list = [f'{var_names[i]} = {var_values[i]}' for i in range(len(rows))]
        
        # Read the existing data.py file (if it exists) and append the new variables to it
        try:
            with open('data.py', 'r') as f:
                existing_vars = f.read()
        except FileNotFoundError:
            existing_vars = ''
        with open('data.py', 'w') as f:
            f.write(existing_vars + '\n' + '\n'.join(var_list))
        
# Call the read_data function to create the variables from the text file
read_data()

@app.route('/', methods=['GET', 'POST']) #decorator
def index():
    data = None
    if request.method == 'POST':
        description = request.form['description']
        data = f'Description: {description}'
        with open('data.txt', 'a') as file:
            file.write(description + '\n')
        # Call the read_data function again to update the variables with the new data
        read_data()
    return render_template('index.html', output=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
