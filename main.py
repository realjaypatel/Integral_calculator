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
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Plot')
    # Convert plot to base64-encoded image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    plt.close()










    return render_template('result.html',plot_url=plot_url , expression=expression, variable=variable, result=result)

@app.route('/integrate', methods=['POST'])
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
    plt.ylabel("$f(x)$")
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


if __name__ == '__main__':
    app.run()
    
