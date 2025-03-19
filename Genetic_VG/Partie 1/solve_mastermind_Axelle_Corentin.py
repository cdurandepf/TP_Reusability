# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""

import mastermind as mm 
import random 


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm 

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher, the better the fitness)
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
    def __init__(self, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        pass  # REPLACE WITH YOUR CODE

    def evolve_for_one_generation(self):
        """ 
            Create the next generation, within the choosen parameter for the selection.

            Args : 
                - None 
            
            Return : 
                - None
        """
        self._population.sort(reverse = True) # sorting the population
        fittest = int(round(self._selection_rate*len(self._population))) # index of last kill
        

        for i in range(fittest) :
            
            index_parent_a = random.randrange(fittest, len(self._population)) #selection of a parent 
            index_parent_b = random.randrange(fittest, len(self._population))

            child = self.cross_population(self._population[index_parent_a], self._population[index_parent_b], self.mutation_rate) #create a child of the next gen
            
            self._population[i] = child




    def cross_population(self, parent_a, parent_b):
        """ 
        Create the new chromosome for the children,
        with the chromosome of the two parents.

        Args : 
            - parent_a : first selected parent 
            - parent_b : second selected parent 
             

        Return :
            - new_individual : is a childrens of the next generation
        """

        
        prob_mutation = random.random() # generate the probability of a mutation

        if prob_mutation < self._mutation_rate :

            valid_colors = mm.getPossibleColors() 
            new_gene = random.choice(valid_colors) # chose the mutation
            position_mutation = random.randrange(0, len(parent_a.chromosome)) #generate the position of the mutation
            new_chrom = parent_a.chromosome[0:position_mutation] + [new_gene] + parent_b.chromosome[position_mutation+1:] 

        else :  
           x_point = random.randrange(0, len(parent_a.chromosome)) # generate the crossing point
           new_chrom = parent_a.chromosome[0:x_point] + parent_b.chromosome[x_point:] # concatenate both parents gene

        new_individual = Individual(new_chrom, MATCH.rate_guess(new_chrom)) # create the new individual
        
        return new_individual



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

    def evolve_until(self, max_nb_of_generations=11500, threshold_fitness=None):
        """ 
        Stop the evolution of our population

        Args : 
            - selection_rate : which part of population will be kill
            - mutation_rate : probability that an individual will mutate 
            - max_nb_of_generations : maximum number of generation 
            - threshold_fitness : sucesse critera 

        Return : 
            - self.get_best_individual() : the best individue
            
        """
        nb_evolution = 0 # keep track of the number of evolution

        while nb_evolution < max_nb_of_generations and self._population[0].fitness < threshold_fitness :
            self.evolve_for_one_generation()
            nb_evolution +=1
            
        return self.get_best_individual()


MATCH = mm.MastermindMatch(secret_size=4) #create a match 

"""
Creation of parameter of a new individual 
"""

chromosome = MATCH.generate_random_guess() 
fitness = MATCH.rate_guess(chromosome)

new_individual = Individual(chromosome, fitness)


#MATCH = mm.MastermindMatch(secretSize=4) 
solver = GASolver()  
solver._population.append(new_individual)
solver.reset_population() 
print(solver.evolve_until(threshold_fitness=MATCH.max_score()) )









