from flask import Flask, render_template, request,send_file
import sympy as sp
import matplotlib.pyplot as plt
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get input from the form
    expression = request.form['expression']
    variable = request.form['variable']

    # Convert input into a sympy expression
    x = sp.symbols(variable)
    integrand = sp.sympify(expression)

    # Calculate the integral
    result = sp.integrate(integrand, x)
    print(result)
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Plot')

    # Save the plot to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    plt.savefig(temp_file.name)
    plt.close()











    return render_template('result.html',img=temp_file , expression=expression, variable=variable, result=result)

@app.route('/plot')
def plot():
    # Generate a simple plot
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Plot')

    # Save the plot to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    plt.savefig(temp_file.name)
    plt.close()

    # Serve the plot file
    return send_file(temp_file.name, mimetype='image/png')
if __name__ == '__main__':
    app.run(debug=True)
