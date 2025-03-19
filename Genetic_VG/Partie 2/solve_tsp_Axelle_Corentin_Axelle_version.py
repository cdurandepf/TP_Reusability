# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""

import mastermind as mm 
import random 
from math import * 
import cities as ct

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
    def __init__(self, selection_rate=0.5, mutation_rate=0.7):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []
        self.road = ct.default_road(ct.load_cities("cities.txt"))

    def reset_population(self, pop_size=200):
        """ Initialize the population with pop_size random Individuals """
        
        for i in range(pop_size):
            new_chrom = random.sample(self.road, len(self.road)) # create a new chromosome
            new_individual = Individual(new_chrom, ct.road_length(ct.load_cities("cities.txt"), new_chrom)) # create a new individual
            self._population.append(new_individual)
        self.show_generation_summary()

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

            child = self.cross_population(self._population[index_parent_a], self._population[index_parent_b]) #create a child of the next gen
            self._population[i] = child
        self.show_generation_summary()




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
        
        x_point = floor(len(parent_a.chromosome)/2) # generate the crossing point
        new_chrom = parent_a.chromosome[0:x_point] 
        for i in range(x_point, len(parent_a.chromosome)) :
            if parent_b.chromosome[i] not in new_chrom :
                new_chrom.append(parent_b.chromosome[i])
        for i in self.road :
            if i not in new_chrom :
                new_chrom.append(i)

        if prob_mutation < self._mutation_rate :
            chang1, chang2 = floor(random.random()*11.999), floor(random.random()*11.999)
            new_chrom[chang1], new_chrom[chang2] = new_chrom[chang2], new_chrom[chang1]

        new_individual = Individual(new_chrom, ct.road_length(ct.load_cities("cities.txt"), new_chrom)) # create the new individual
        
        return new_individual



    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        # print("population : ", self._population)
        # print("best individual : ", self.get_best_individual())
        # print([len(self._population[i].chromosome) for i in range(len(self._population))])
        pass

    def get_best_individual(self):
        """ 
        Args : 
            - None

        Return :
            - self._population[0] : the individual with the best fitness 
        """
        self._population.sort() 

        return self._population[0]

    def evolve_until(self, max_nb_of_generations=100, threshold_fitness=None):
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
        if threshold_fitness == None :
            while nb_evolution < max_nb_of_generations :
                self.evolve_for_one_generation()
                nb_evolution +=1
        else : 
            while nb_evolution < max_nb_of_generations and self._population[0].fitness < threshold_fitness :
                self.evolve_for_one_generation()
                nb_evolution +=1
                
        return self.get_best_individual()


"""
Creation of parameter of a new individual 
"""

chromosome = ct.default_road(ct.load_cities("cities.txt"))
fitness = ct.road_length(ct.load_cities("cities.txt"), chromosome)

new_individual = Individual(chromosome, fitness)


solver = GASolver()  
solver._population.append(new_individual)
solver.reset_population() 
print(solver.evolve_until() )
ct.draw_cities(ct.load_cities("cities.txt"), solver.get_best_individual().chromosome)