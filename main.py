import random
import numpy as np
import pandas as pd

# Implement Rposenbrock function
def fitness_f1(individuals):
    return sum(100.0*(individuals[1:]-individuals[:-1]**2.0)**2.0 + (1-individuals[:-1])**2.0)

# Implement Griewanks function
def fitness_f2(individuals):
    sum = 0
    prod = 1
    for i in range(len(individuals)):
        sum += individuals[i]**2/4000
        prod *= np.cos(individuals[i]/np.sqrt(i+1))
    return sum - prod + 1

def objective_function(individuals):
    return [fitness_f1(individuals) , fitness_f2(individuals)]

def EP_process(generations, bound, parameters):
    # Extract parameters
    population_size = parameters[0]
    generations = parameters[1]
    dim = parameters[2]

    # Create the initial particle and variance of the population
    solution_vector = np.random.uniform(low=bound[0], high=bound[1], size=(population_size, dim))
    variancevector = np.var(solution_vector, axis=0)

    for generation in generations:
            print(f'Generation: {generation} of {generations} ...')
            
            # Evaluate the fitness of each dimention in the population
            """
                FITNESS FUNCTION
                    - Fitness function is used to evaluate the fitness of the population.
                    - Store the fitness value of the offsprings into a new variable
            """
            #fitness = [objective_function(solution) for solution in solution_vector]
            
            
            """
                MUTATION 
                    - Mutation Type (crunchy function) 
                    - Mutation function is used to create new offsprings from the current population
                    - Store the new offsprings into a new variable
            """
            #offspring_vector = [mutation(solution, variancevector) for solution in solution_vector]
            """
                FITNESS FUNCTION
                    - Fitness function is used to evaluate the fitness of the offsprings
                    - Store the fitness value of the offsprings into a new variable
            """
            #pffspring_fitness = [objective_function(offspring) for offspring in offspring_vector]
            """
                COMBINANTION OF POPULATION AND OFFSPRING
                    - Combine the population and the offsprings
            """
            """
                SELECTION FUNCTION
                    - Selection function is used to select the best individuals from the population and the offspring population
                    - Store the selected individuals into a new variable
                    - Store variance of the selected individuals into a new variable.
            """
            #selected_individuals = selection(fitness, pffspring_fitness, solution_vector, offspring_vector, variancevector)
            """
                UPDATE POPULATION
                    - Update the population with the selected individuals
            """
            # Update the population and variance of the population
            #solution_vector = selected_individuals

            # Track the best solution: store the best solution and variance of the best solution
            #best_solution = np.min(fitness)
            #best_variances = np.min(variancevector)

def ES_process(generations, bound, parameters):
    # Extract parameters
    population_size = parameters[0]
    generations = parameters[1]
    dim = parameters[2]

    # Create the initial particle and variance of the population
    solution_vector = np.random.uniform(low=bound[0], high=bound[1], size=(population_size, dim))
    variancevector = np.var(solution_vector, axis=0)

    for generation in generations:


def main():
    # General Parameters 
    population_size = 50   
    generations = 100  

    # Solution Boundary 
    bound = [-30, 30]   # Lower bound and Upper bound of the search space
    runs = 30   
    dim = [20, 50]   # Dimension of the problem

    for run in runs:
        # Loop through the dimension, 20 and 50
        for dim_ in dim:

            # EP optimization process
            EP_parameters = [generations, population_size]
            EP_process(bound, EP_parameters)

            # ES optimization process
            μ = 10  # Parents
            λ = 50  # Offspring
            ES_parameters = [population_size, generations, dim_, μ, λ]
            ES_process(bound, ES_parameters)
        





if __name__ == "__main__":
    main()