# -*- coding: utf-8 -*-
"""
Created on Thuesday 26-02-2025

@author: DURAND & BROSSE

Exercise 3 submission 
(generic genetic algorithm module)
"""

########################################################################################################
"IMPORT"                                                                                                
########################################################################################################

import random
#import fichier as f
import math
import tkinter as tk
from tkinter import messagebox
import mm_correct as mm

########################################################################################################
"CLASS"
########################################################################################################

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
class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    # illustrate how the generation are created ?? 
    #mutation , reproduction , , what are the variable  on doit juste changer ca pr que ca marche 
    # specify what we nee d to have to complete the problem 
    #Never Grad ( exemple )
    """#####################################################################################################
    #INITIALIZATION
    #####################################################################################################"""

    def __init__(self, selection_rate = 0.5, mutation_rate = 0.7):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []
        self.chromosome_code = ""
        self.fitness_code = ""
        self.crossover_code = ""
        self.solution = ["blue", "blue", "blue", "blue"]
        self.first = True
        self.secret = []
        self.temp_chrom = []
        self.temp_fit = 1000
        self.temp_indiv = Individual(self.temp_chrom, self.temp_fit)
        self.temp_indiv_chrom = []

    """#####################################################################################################
    #METHODS
    #####################################################################################################"""
    
    def interface(self): 
        

        # Global variables to store user-defined functions
        chromosome_code = ""
        fitness_code = ""
        crossover_code = ""
        global step 
        step = 1  # Track which function the user is writing

        # Create main window
        root = tk.Tk()
        root.title("Genetic Algorithm Functions")
        root.geometry("600x400")

        # Instruction label
        global label
        self.label = tk.Label(root, text="Step 1: Write the Chromosome Function")
        self.label.pack(pady=5)

        # Text entry widget
        global text_entry
        self.text_entry = tk.Text(root, height=10, width=60)
        self.text_entry.pack(pady=10)

        # Submit button
        global submit_button
        self.submit_button = tk.Button(root, text="Next", command=self.next_step)
        self.submit_button.pack()

        # Run the main event loop
        root.mainloop()



    def next_step(self):
        global step, chromosome_code, fitness_code, crossover_code
        
        #code = mm.code_mm()

        user_code = self.text_entry.get("1.0", tk.END).strip()  # Get user input
        if step == 1:
            self.chromosome_code = user_code  # Store Chromosome function
            #self.chromosome_code = code[0]
            self.label.config(text="Step 2: Write the Fitness Function")
        elif step == 2:
            self.fitness_code = user_code  # Store Fitness function
            #self.fitness_code = code[1]
            self.label.config(text="Step 3: Write the Crossover Function")
        elif step == 3:
            self.crossover_code = user_code  # Store Crossover function
            #self.crossover_codero = code[2]
            self.execute_functions()
            return [self.chromosome_code, self.fitness_code, self.crossover_code]
        
        step += 1
        self.text_entry.delete("1.0", tk.END)  # Clear text box for the next function
    

    def execute_functions(self):
        # try:
        #     # Execute each function in global scope
        #     # exec(self.chromosome_code, globals())
        #     # exec(self.fitness_code, globals())
        #     # exec(self.crossover_code, globals())

        #     messagebox.showinfo("Success", "All functions executed successfully!")
        # except Exception as e:
        #     messagebox.showerror("Error", f"An error occurred:\n{e}")
        pass


    def generate_chromosom(self):
        """Generate a random individual."""
        shared_namespace = {
            "self": self
        }
        result = exec(self.chromosome_code, shared_namespace)        
        self.first = False
        return self.temp_chrom
        
    
        #exec(self.chromosome_code, globals())

    def fitness(self,chrom):
        """Evaluate the fitness of an individual."""
        shared_namespace = {
            "self": self,
            "chrom": chrom,  
            "solution": self.solution
        }
        # print(self.generate_chromosom())
        # print(self.solution)
        # print(self.chromosome_code)
        exec(self.fitness_code, shared_namespace)
        return self.temp_fit
    
    def generate_individual(self):
        """Generate a random individual."""
        new_individual = Individual(self.generate_chromosom(), self.fitness(self.generate_chromosom()))
        return new_individual

    def crossover(self, parent_a, parent_b, mutation_rate):
        shared_namespace = {
            "self": self,
            "parent_a": parent_a,  
            "parent_b": parent_b,  
            "mutation_rate": mutation_rate
        }
        """Perform crossover between two parents to produce offspring."""
        exec(self.crossover_code, shared_namespace)
        new_individual = Individual(self.temp_indiv_chrom, self.fitness(self.temp_indiv_chrom))
        return  new_individual

    # def is_solution(self):
    #     """Check if an individual is a solution."""
    #     solver = GASolver(self)
    #     return(solver.evolve_untill())


