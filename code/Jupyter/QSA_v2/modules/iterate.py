from .ConstantsAndParameters import *
from .model import *

# define pure iterative loop
# should be the same as the pure iteration
def pure_iterative(init_values, parameters, set_of_equations, iteration_sett):
    errii  = iteration_sett[0] # get the error for which the loop is interrupted
    maxii  = iteration_sett[1] # get the maximum number of iteration for the loop
    
    ii = 0
    # dd[ 'iteration number', 'data class (Up/Us/Ut/...)']
    all_data = np.array([init_values]) # init values ~ ('Up', 'Us', 'Ut', 'ΔN', 'ΔT', 'Δω')
    ii += 1
    
    ### execute first iteration and store data
    all_data = np.vstack([all_data, set_of_equations(init_values, parameters)])
    ii += 1
    
    ### store new values
    
    # enter loop
    while (np.amax(np.abs(all_data[-1,:]-all_data[-2,:])) >= errii) & (ii<maxii):
        ii += 1
        
        ### put old data in vector, to become input of equations()
        old_var = all_data[-1,:]
        
        ### generate new values and store them
        all_data = np.vstack([all_data, set_of_equations(old_var, parameters)])
        #new_data = set_of_equations(init_values, parameters)
        #np.vstack([data, new_data])
        
    return (all_data, ii)

# define first genetic algorithm
# mixes the last two output values as inputs for the next step
# pure_iterative(...) should be the same as genetic2(..., type=0)
def genetic2(init_values, parameters, set_of_equations, iteration_sett):
    errii = iteration_sett[0] # get the error for which the loop is interrupted
    maxii = iteration_sett[1] # get the maximum number of iteration for the loop
    weight = iteration_sett[2] # get the weight of the history
    
    ii = 0
    # dd[ 'iteration number', 'data class (Up/Us/Ut/...)']
    all_data = np.array([init_values]) # init values ~ ('Up', 'Us', 'Ut', 'ΔN', 'ΔT', 'Δω')
    ii += 1
    
    ### execute first iteration and store data
    all_data = np.vstack([all_data, set_of_equations(init_values, parameters)])
    ii += 1
    
    ### store new values
    
    # enter loop
    while (np.amax(np.abs(all_data[-1,:]-all_data[-2,:])) >= errii) & (ii<maxii):
        ii += 1
        
        ### put old data in vector, to become input of equations()
        old_var = (1.0-weight)*all_data[-1,:] + weight*all_data[-2,:]
        
        ### generate new values and store them
        all_data = np.vstack([all_data, set_of_equations(old_var, parameters)])
    
    return (all_data, ii)

def next_algorithm():
    print("not implemented yet")

# map the inputs to the function blocks
options = {0 : pure_iterative,
           2 : genetic2,
           3 : next_algorithm,
}

def iterator(variables, parameters, system_to_solve = norm_single_source, type = 0, err_it = 1e-6, max_it = 5e2, weight = 0):
    return options[type](variables, parameters, system_to_solve, (err_it, max_it, weight))


