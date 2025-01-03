# Graphical method to solve linear programming problems
# Graphical method type: Extreme Point Approach
# Author: Jubran Akram (github.com/jubranakram)
# -----------------------------------------------------
# Steps:
# 1. Draw an x1-x2 plane and select the set of points satisfying the non-negative constraints x1 >= 0 and x2 >= 0.
# 2. Draw all constraints as lines on the x1-x2 plane, and identify the common (feasible) region.
# 3. Identify the extreme points (corner points) of the feasible region. 
#    Evaluate the objective function at each extreme point. Select the point which optimizes the objective function.
# 4. Interpret the results.
# -----------------------------------------------------

from utils.common_utils import (
    evaluate_linear_equation as elq,
    plot_line_through_points as pltp,
    plot_single_line as plsl,
    get_intersection_point as gip,
    plot_both_lines as pbl,
    evaluate_extreme_points as eep,
    load_inputs
)

# Example:
# Maximize Total revenue (R) = 45x1 + 80x2
# Subject to:
# 1. 5x1 + 20x2 <= 400
# 2. 10x1 + 15x2 <= 450
# 3. x1 >= 0, x2 >= 0
if __name__ == '__main__':
    # Input YAML file path
    input_file = './01_graphical_method_extreme_points.yml'
    parameters = load_inputs(input_file)
    line_1 = parameters.get('lines')[0]
    line_2 = parameters.get('lines')[1]
    plot_1 = parameters.get('plots')[0]
    plot_2 = parameters.get('plots')[1]
    plot_3 = parameters.get('plots')[2]
    
    # Step 2: Draw all constraints and identify feasible region
    # Constraint # 1
    plsl(*line_1.get('coefficients').values(), plot_1.get('title'), line_1.get('color'), 
         '', plot_1.get('output_filepath'))
    # Constraint # 2
    plsl(*line_2.get('coefficients').values(), plot_2.get('title'), line_2.get('color'), 
         '', plot_2.get('output_filepath'))
    # Combined plot for common region
    pbl(line_1, line_2, plot_3)
    
    # Identify the extreme points of the feasible region
    # From graph_method_all_constraints.png, the extreme points are:
    pts = [(0, 0), (0, 20), (45, 0), (24, 14)]
    objective_fun = lambda x1, x2: 45*x1 + 80*x2
    
    # Evaluate the objective function at each extreme point
    max_fun_value, max_pts, fun_values = eep(objective_fun, pts, 'max')
    print(f"Maximum value of the objective function: {max_fun_value}")
    print(f"Optimal point(s): {max_pts}")
    print(f"Function values at extreme points: {fun_values}")
    
    if len(max_pts) > 1:
        print("Multiple optimal solutions exist. Interpret carefully.")
    else:
        print(f"The optimal value {max_fun_value} exists at point {max_pts[0]}")
    
    