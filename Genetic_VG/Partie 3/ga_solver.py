# -*- coding: utf-8 -*-
"""
Created on Thuesday 26-02-2025

@author: DURAND & BROSSE

Exercise 3 submission 
(generic genetic algorithm module)
"""

#####################################################
"IMPORT"                                                                                                 
#####################################################

import random 
import ga_problem as gp

#####################################################
"CLASS"
#####################################################

class Individual:
    """Represents an Individual for a genetic algorithm"""

    #####################################################
    "INITIALIZATION"
    #####################################################

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GASolver: 

    ##################################################
    "INITIALIZATION"
    #####################################################

    def __init__(self, GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = GAProblem()
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []
        self._problem.interface()
    #####################################################
    "METHODS SETUP"
    #####################################################

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size):
            new_chrom = self._problem.generate_chromosom() # create a new chromosome
            new_individual = Individual(new_chrom, self._problem.fitness(new_chrom)) # create a new individual
            self._population.append(new_individual)
    
    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE
    
    def get_best_individual(self):
         """ 
        Args : 
            - None

        Return :
            - self._population[0] : the individual with the best fitness 
        """
         self._population.sort() 
         return self._population[0]

    #####################################################
    "METHOD EVOLUTION"
    #####################################################

    def evolve_for_one_generation(self):
        """ 
            Create the next generation, within the choosen parameter for the selection.

            Args : 
                - None 
            
            Return : 
                - None
        """  
        self._population.sort(reverse = True) # sorting the population
        index_fit = int(round(self._selection_rate*len(self._population))) # index of last kill
        

        for i in range(len(self._population) - index_fit) :
            
            index_parent_a = random.randrange(index_fit, len(self._population)) #selection of a parent 
            index_parent_b = random.randrange(index_fit, len(self._population))

            child = self._problem.crossover(self._population[index_parent_a], self._population[index_parent_b], self._mutation_rate) #create a child of the next gen
            
            self._population[i] = child

    def evolve_until(self, max_nb_of_generations=10, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
    
            - selection_rate : which part of population will be kill
            - mutation_rate : probability that an individual will mutate 
            - max_nb_of_generations : maximum number of generation 
            - threshold_fitness : sucesse critera 

        Return : 
            - self.get_best_individual() : the best individue
            
        """
        nb_evolution = 0 # keep track of the number of evolution
        if threshold_fitness == None :
            while nb_evolution < max_nb_of_generations :
                #if self._population[0].fitness < threshold_fitness :
                #   nb_evolution = max_nb_of_generations
                self.evolve_for_one_generation()
                nb_evolution += 1
        else : 
            while nb_evolution < max_nb_of_generations and self.get_best_individual().fitness < threshold_fitness :
                #if self._population[0].fitness < threshold_fitness :
                #   nb_evolution = max_nb_of_generations
                self.evolve_for_one_generation()
                nb_evolution += 1
            
        return self.get_best_individual()
    

#Script

solver = GASolver(gp.GAProblem)
solver.reset_population()
print(solver.evolve_until())