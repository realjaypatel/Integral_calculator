from flask import Flask, render_template,request
import sympy as sp
import matplotlib.pyplot as plt
import io
import base64
app = Flask(__name__)


from sympy.utilities.lambdify import lambdify
from sympy import *
from numpy import *
from scipy.integrate import *
import math, scipy
from scipy import integrate
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import warnings
warnings.filterwarnings("ignore") 


# def integrate_with_graph():
#     def g(x):
#         func = eval(abc)
#         return func
#     print()
#     print("Enter the function you want to see graphed and INTEGRATED!")
#     aba = input()
#     abc = aba.replace("^", "**")
#     print("Enter the lower bound: ")
#     low = float(input())
#     print("Enter the upper bound: ")
#     upp = float(input())
#     if(("1/x" in aba or aba == "x^-1") and (low <= 0 or upp <= low+1)):
#         return("This integral is divergent. It cannot be computed as of now.")
#     x = np.linspace(int(floor(low))-8, int(ceil(upp))+8, 20000)
#     if("ln" in aba or "log" in aba):
#         x = np.linspace(int(floor(low))+1, int(ceil(upp))+8, 20000)
#     #x = range(int(floor(low))-4, int(ceil(upp))+4)
#     # Get the corresponding y values from the function
#     y = [g(a) for a in x]
#     # Set up the plot
#     fig, ax = plt.subplots()
#     plt.xlabel('$x$')
#     plt.ylabel("$f(x)$")
#     plt.grid()
#     # Plot x against g(x)
#     plt.plot(x,y, color='orange')
#     # Make the shaded region
#     ix = np.linspace(low, upp)
#     #print("About to create a list of all values")
#     iy = [g(i) for i in ix]
#     verts = [(low, 0)] + list(zip(ix, iy)) + [(upp, 0)]
#     poly = Polygon(verts, facecolor='cyan')
#     ax.add_patch(poly)
#     try:
#         print("Here is the shaded area under the curve! Close it to see the calculated integral.")
#         plt.show()
#         ab, bc = quad(g, low, upp)
#         print('abbc',ab,bc)
#         int_statement = "The calculated integral of " +aba+" from "+str(low)+" to "+str(upp)+" is: " + str(ab) +"."
#         return(int_statement)
#     except:
#         print("This integral is divergent!")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inti', methods=['POST'])
def calculate():
    # Get input from the form
    fxn = request.form['fxn']
    variable = request.form['variable']
    plot_url = '1'
    aba = fxn
    abc = aba.replace("^", "**")
    def g(x):
        func = eval(abc)
        return func


    # Convert input into a sympy fxn
    x = sp.symbols(variable)
    integrand = sp.sympify(fxn)

    # Calculate the integral
    result = sp.integrate(integrand, x)
    
    x = np.linspace(-8, 10+8, 20000)
    if("ln" in aba or "log" in aba):
        x = np.linspace(1, 10+8, 20000)
    y = [g(a) for a in x]
    fig, ax = plt.subplots()
    plt.xlabel('$x$')
    plt.ylabel(aba)
    plt.grid()
    plt.plot(x,y, color='orange')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return render_template('result.html',plot_url=plot_url , fxn=fxn, variable=variable, result=result)

@app.route('/definti', methods=['POST'])
def intigrate():
    # Get input from the form
    fxn = request.form['fxn']
    lowerBound = request.form['lowerBound']
    upperBound = request.form['upperBound']
    plot_url = '1'

   
    def g(x):
        func = eval(abc)
        return func


    aba = fxn
    abc = aba.replace("^", "**")
    low = float(lowerBound)
    upp = float(upperBound)
    if(("1/x" in aba or aba == "x^-1") and (low <= 0 or upp <= low+1)):
        return render_template('result.html',plot_url=plot_url , fxn = request.form['fxn'],lowerBound = request.form['lowerBound'],upperBound = request.form['upperBound'],result="This integral is divergent. It cannot be computed as of now.")


    x = np.linspace(int(floor(low))-8, int(ceil(upp))+8, 20000)
    if("ln" in aba or "log" in aba):
        x = np.linspace(int(floor(low))+1, int(ceil(upp))+8, 20000)
    #x = range(int(floor(low))-4, int(ceil(upp))+4)
    # Get the corresponding y values from the function
    y = [g(a) for a in x]
    # Set up the plot
    fig, ax = plt.subplots()
    plt.xlabel('$x$')
    plt.ylabel(aba)
    plt.grid()
    plt.plot(x,y, color='orange')
    ix = np.linspace(low, upp)
    iy = [g(i) for i in ix]
    verts = [(low, 0)] + list(zip(ix, iy)) + [(upp, 0)]
    poly = Polygon(verts, facecolor='cyan')
    ax.add_patch(poly)
    try:
        # print("Here is the shaded area under the curve! Close it to see the calculated integral.")
        # plt.show()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        plt.close()
        ab, bc = quad(g, low, upp)
        return render_template('result.html',plot_url=plot_url , fxn = request.form['fxn'],lowerBound = request.form['lowerBound'],upperBound = request.form['upperBound'],result= str(ab))
    # (int_statement)
    except:
        return render_template('result.html',plot_url=plot_url , fxn = request.form['fxn'],lowerBound = request.form['lowerBound'],upperBound = request.form['upperBound'],result="This integral is divergent! It cannot be computed as of now.")





    return render_template('result.html',plot_url=plot_url , fxn = request.form['fxn'],lowerBound = request.form['lowerBound'],upperBound = request.form['upperBound'],result="This integral is divergent. It cannot be computed as of now.")


@app.route('/diff', methods=['POST'])
def diff():
    
    # Get input from the form
    fxn = request.form['fxn']
    variable = request.form['variable']
    plot_url = '1'
    aba = fxn
    abc = aba.replace("^", "**")
    def g(x):
        func = eval(abc)
        return func


    # Convert input into a sympy fxn
    x = sp.symbols(variable)
    integrand = sp.sympify(fxn)

    # Calculate the integral
    result = sp.diff(integrand, x)
    
    x = np.linspace(-8, 10+8, 20000)
    if("ln" in aba or "log" in aba):
        x = np.linspace(1, 10+8, 20000)
    y = [g(a) for a in x]
    fig, ax = plt.subplots()
    plt.xlabel('$x$')
    plt.ylabel(aba)
    plt.grid()
    plt.plot(x,y, color='orange')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return render_template('result.html',plot_url=plot_url , fxn=fxn, variable=variable, result=result)

@app.route('/defdiff', methods=['POST'])
def defdiff():
    fxn = request.form['fxn']
    variable = request.form['variable']
    value = float(request.form['value'])
    plot_url = '1'
    x = sp.symbols(variable)
    f = sp.sympify(fxn)
    df = sp.diff(f, x)
    x = sp.symbols(variable)
    f = sp.sympify(fxn)
    result = f.subs({x: value})

    x_vals = np.linspace(value - 2, value + 2, 100)
    x = sp.symbols(variable)
    f = sp.sympify(fxn)
    f_lambda = sp.lambdify(x, f, modules=['numpy'])
    tangent_line = df.subs({x: value}) * (x_vals - value) + f_lambda(value)

    plt.plot(x_vals, f_lambda(x_vals), label='Function')
    plt.plot(x_vals, tangent_line, label='Tangent at x={}'.format(value))
    plt.scatter(value, result, color='red')

    plt.legend()
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function and Tangent Line')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return render_template('result.html',plot_url=plot_url , fxn=fxn, lowerBound=df, result=result)






















    # fxn = request.form['fxn']
    # variable = request.form['variable']
    # value = request.form['value']
    # plot_url = '1'
    # aba = fxn
    # abc = aba.replace("^", "**")
    # def g(x):
    #     func = eval(abc)
    #     return func


    # # Convert input into a sympy fxn
    # x = sp.symbols(variable)
    # integrand = sp.sympify(fxn)

    # # Calculate the integral
    # result = sp.diff(integrand, x)
    
    # x = np.linspace(-8, 10+8, 20000)
    # if("ln" in aba or "log" in aba):
    #     x = np.linspace(1, 10+8, 20000)
    # y = [g(a) for a in x]
    # fig, ax = plt.subplots()
    # plt.xlabel('$x$')
    # plt.ylabel(aba)
    # plt.grid()
    # plt.plot(x,y, color='orange')
    
    # # Define symbol and fxn

    # x = sp.symbols(variable)
    # expr = sp.sympify(fxn)
    # x_val = value

    # # Calculate the derivative
    # derivative = sp.diff(expr, x)
    # print("Derivative:", derivative)

    # # Evaluate the derivative at the given point
    # derivative_at_point = derivative.evalf(subs={x: x_val})
    # return render_template('result.html',plot_url=plot_url , fxn=fxn, variable=variable, result=derivative_at_point)

def differential_calculator(fxn, variable):
    x = sp.symbols(variable)
    f = sp.sympify(fxn)
    df = sp.diff(f, x)
    return df

def evaluate_fxn(fxn, variable, value):
    x = sp.symbols(variable)
    f = sp.sympify(fxn)
    result = f.subs({x: value})
    return result

if __name__ == '__main__':
    app.run(debug=True)
    
