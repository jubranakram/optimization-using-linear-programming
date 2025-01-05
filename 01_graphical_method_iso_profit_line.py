# Graphical method to solve linear programming problems
# Graphical method type: ISO-Profit (Cost) Line Approach
# Author: Jubran Akram (github.com/jubranakram)
# -----------------------------------------------------
# Steps:
# 1. Draw an x1-x2 plane and select the set of points satisfying the non-negative constraints x1 >= 0 and x2 >= 0.
# 2. Draw all constraints as lines on the x1-x2 plane, and identify the common (feasible) region.
# 3. Draw an ISO-Profit (Cost) line on the x1-x2 plane for a small value of the objective function, without 
#    violating any of the given restrictions of the given LPP.
# 4. Continue drawing ISO-Profit (Cost) lines parallel to the first line in the direction of increasing or 
#    decreasing value of the objective function
# 5. Identify the last line that touches the feasible region and the corresponding is referred to as the optimal solution.
# -----------------------------------------------------

import numpy as np
from utils.common_utils import (
    evaluate_linear_equation as elq,
    plot_line_through_points as pltp,
    plot_single_line as plsl,
    get_intersection_point as gip,
    plot_both_lines as pbl,
    evaluate_extreme_points as eep,
    load_inputs
)

def update_line_title(title: str, value: float) -> str:
    """
    Update the title of the plot.
    Args:
        title (str): The title of the plot.
        value (float): The value of the objective function.
    Returns:
        str: The updated title of the plot.
    """
    updated_title = title.replace(title.split(' = ')[-1], f'{value:.1f}$')
    return updated_title

# Example:
# Maximize Total revenue (R) = 45x1 + 80x2
# Subject to:
# 1. 5x1 + 20x2 <= 400
# 2. 10x1 + 15x2 <= 450
# 3. x1 >= 0, x2 >= 0
if __name__ == '__main__':
    # Input YAML file path
    input_file = './01_graphical_method_iso_profit_line.yml'
    parameters = load_inputs(input_file)
    line_1 = parameters.get('lines')[0]
    line_2 = parameters.get('lines')[1]
    line_3 = parameters.get('lines')[2]
    plot_1 = parameters.get('plots')[0]
    plot_2 = parameters.get('plots')[1]
    plot_3 = parameters.get('plots')[2]
    plot_4 = parameters.get('plots')[3]
    plot_5 = parameters.get('plots')[4]
    
    # Step 2: Draw all constraints and identify feasible region
    # Constraint # 1
    plsl(*line_1.get('coefficients').values(), plot_1.get('title'), line_1.get('color'), 
         '', plot_1.get('output_filepath'))
    # Constraint # 2
    plsl(*line_2.get('coefficients').values(), plot_2.get('title'), line_2.get('color'), 
         '', plot_2.get('output_filepath'))
    # Combined plot for common region
    pbl(line_1, line_2, plot_3)
    
    # Step 3: Draw an ISO-Profit (Cost) line on the x1-x2 plane for a small value of the 
    # objective function, without violating any of the given restrictions of the given LPP.
    plsl(*line_3.get('coefficients').values(), plot_4.get('title'), line_3.get('color'), 
         line_3.get('title'), plot_4.get('output_filepath'), 0)
    # Step 4: Continue drawing ISO-Profit (Cost) lines parallel to the first line in the 
    # direction of increasing objective function value (as suggested by the figure, graph_method_iso_profilt_line.png)
    initial_value = line_3.get('coefficients').get('c')
    lines = np.arange(initial_value+line_3.get('step'), line_3.get('max_value')+line_3.get('step'), line_3.get('step'))
    colors = ['magenta', 'black', 'brown', 'purple', 'orange', 'skyblue']
    coeffs = line_3.get('coefficients').copy()    
    for l, c in zip(lines, colors):
        coeffs.update({'c': l})
        plsl(*coeffs.values(), plot_5.get('title'), c, 
             update_line_title(line_3.get('title'), l), plot_5.get('output_filepath'), 0)
    
    # Step 5: Identify the last line that touches the feasible region and 
    # the corresponding point(s) is referred to as the optimal solution.
    
    