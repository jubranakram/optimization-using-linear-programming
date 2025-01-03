# Author: Jubran Akram (github.com/jubranakram)
import numpy as np
import yaml

import matplotlib.pyplot as plt

def evaluate_linear_equation(a: float, b: float, c: float) -> tuple:
    """
    Evaluate the linear equation of the form ax + by = c and return the intercepts.
    This function calculates the intercepts of the linear equation with the x-axis and y-axis.
    It returns the points where the line intersects the axes.
    Args:
        a (float): Coefficient of x in the equation.
        b (float): Coefficient of y in the equation.
        c (float): Constant term in the equation.
    Returns:
        tuple: A tuple containing two tuples:
            - (0, y1): The point where the line intersects the y-axis.
            - (x2, 0): The point where the line intersects the x-axis.
    Note:
        If `b` is zero, the y-intercept is set to 0.
        If `a` is zero, the x-intercept is set to 0.
    Examples:
        >>> evaluate_linear_equation(2, 3, 6)
        ((0, 2.0), (3.0, 0))
        >>> evaluate_linear_equation(1, 0, 4)
        ((0, 0), (4.0, 0))
        >>> evaluate_linear_equation(0, 1, 5)
        ((0, 5.0), (0, 0))
    """
    
    # For x1 = 0
    y1 = c / b if b != 0 else 0
    # For x2 = 0
    y2 = c / a if a != 0 else 0
    return (0, y1), (y2, 0)

def plot_line_through_points(point1: tuple, point2: tuple, title: str,                           
                             color: str='b', label: str=None, 
                             output: str=None, ax:int=1):
    """
    Plots a line through two given points on a 2D plane.
    Args:
        point1 (tuple): The first point as a tuple (x, y).
        point2 (tuple): The second point as a tuple (x, y).
        title (str): The title of the plot.
        color (str, optional): The color of the line. Defaults to 'b'.
        label (str, optional): The label for the line. Defaults to None.
        output (str, optional): The file path to save the plot. Defaults to None.
        ax (int, optional): If 1, creates a new figure. Defaults to 1.
    Returns:
        None
    """    
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    if ax:
        plt.figure()
    plt.plot(x_values, y_values, marker='o', color=color, label=f'{label}' if label else '_nolegend_')
    plt.axhline(0, color='black',linewidth=0.2)
    plt.axvline(0, color='black',linewidth=0.2)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.text(point1[0], point1[1], f'({point1[0]}, {point1[1]:.2f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    plt.text(point2[0], point2[1], f'({point2[0]:.2f}, {point2[1]})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.legend()
    plt.title(f"{title}")
    if output is not None:
        plt.savefig(output)    
        
def plot_single_line(a: float, b: float, c: float, 
                     title: str, color: str='b', 
                     label:str=None, output:str=None, ax: int=1):
    """
    Evaluate the linear equation of the form ax + by = c and 
    plots a line through two given points on a 2D plane.
    Args:
        a (float): Coefficient of x in the equation.
        b (float): Coefficient of y in the equation.
        c (float): Constant term in the equation.
        title (str): The title of the plot.
        color (str, optional): The color of the line. Defaults to 'b'.
        label (str, optional): The label for the line. Defaults to None.
        output (str, optional): The file path to save the plot. Defaults to None.
        ax (int, optional): If 1, creates a new figure. Defaults to 1.
    Returns:
        None
    """
    point1, point2 = evaluate_linear_equation(a, b, c)
    plot_line_through_points(point1, point2, title, color, label, output, ax)
    
def get_intersection_point(a, b, c, d, e, f):
    """
    Solves for the intersection point of two lines given by the equations:
    a*x + b*y = c
    d*x + e*y = f
    Parameters:
    a (float): Coefficient of x in the first equation.
    b (float): Coefficient of y in the first equation.
    c (float): Constant term in the first equation.
    d (float): Coefficient of x in the second equation.
    e (float): Coefficient of y in the second equation.
    f (float): Constant term in the second equation.
    Returns:
    numpy.ndarray: A 1D array containing the x and y coordinates of the intersection point.
    Raises:
    numpy.linalg.LinAlgError: If the equations are parallel or otherwise unsolvable.
    """
    try:
        A = np.array([[a, b], [d, e]])
        b = np.array([c, f])
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        print(f"Error: {e}")
        return None
    
def load_inputs(input_file: str) -> dict:
    """
    Load input data from a YAML file.
    Args:
        input_file (str): The path to the input YAML file.
    Returns:
        dict: A dictionary containing the input data.
    """
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)
    return data

def plot_both_lines(line_1: dict, line_2: dict, plot_3: dict):
    """
    Plots both constraints together
    Args:
        line_1 (dict): The parameters for the first line.
        line_2 (dict): The parameters for the second line.
        plot_3 (dict): The parameters for the combined plot.
    Returns:
        None
    """
    # Constraint # 1
    plot_single_line(*line_1.get('coefficients').values(), plot_3.get('title'), 
                     line_1.get('color'), line_1.get('title'))
    pt = get_intersection_point(*line_1.get('coefficients').values(), 
                                *line_2.get('coefficients').values())
    if pt is not None:
        if pt[0] >= 0 and pt[1] >= 0:
            plt.plot(pt[0], pt[1], marker='o', color='g')
            plt.text(pt[0], pt[1], f'({pt[0]}, {pt[1]:.2f})', fontsize=9, verticalalignment='top', horizontalalignment='right')
            print(f"Intersection point: {pt}")
    # Constraint # 2
    plot_single_line(*line_2.get('coefficients').values(), plot_3.get('title'), 
                     line_2.get('color'), line_2.get('title'), plot_3.get('output_filepath'), 0)
    
def evaluate_extreme_points(fun, pts: list[tuple], type: str='max') -> tuple:
    """
    Evaluate the objective function at each extreme point and return the maximum value.
    Args:
        fun (function): The objective function to be evaluated.
        pts (list): A list of tuples representing the extreme points.
        type (str, optional): The type of extreme point to be evaluated. Defaults to 'max'.
    Returns:
        tuple: A tuple containing the maximum value and the point where it occurs, 
               also the list of function values at extreme points.
    """
    fun_values = [fun(*pt) for pt in pts]
    opt_fun_value = np.max(fun_values) if type == 'max' else np.min(fun_values)
    # check how many instance of optimal values occur
    opt_instances = np.where(fun_values == opt_fun_value)[0]
    opt_pts = []
    if len(opt_instances) > 1:
        for val in opt_instances:
            opt_pts.append(pts[val])
    else:
        opt_pts.append(pts[opt_instances[0]])
    return opt_fun_value, opt_pts, fun_values
    