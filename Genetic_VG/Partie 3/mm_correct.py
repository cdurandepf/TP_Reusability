
def code_mm() :
    code_1 = """
def generate_random_guess(self):
    from random import choice
    _colors = ['blue', 'red', 'green', 'yellow', 'orange', 'violet']
    secret = [choice(_colors) for _ in range(4)]
    if self.first : 
        self.solution = [choice(_colors) for _ in range(4)]
    self.temp_chrom = secret
generate_random_guess(self)
    """
    code_2 = """
def rate_guess(self, chrom):
    correct_position = 0
    correct_colors = 0
    count = 0
    for color in chrom:
        if solution[count] == color:
            correct_position += 1
        elif color in solution:
            correct_colors += 1
        count += 1
    score = correct_colors*1 + correct_position *3
    self.temp_fit = score
rate_guess(self, chrom)
    """

    code_3 = """
def cross_population(self, parent_a, parent_b):       
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
    self.temp_indiv =  new_individual
cross_population(self,parent_a, parent_b)
    """
    return [code_1, code_2, code_3]
