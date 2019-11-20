import string
import numpy as np

# initializing list of lower case letters
chars = list(string.ascii_lowercase) + list(string.whitespace[0])

# initializing parameters
target_sentence = "i am trying to learn evolutionary algorithm"
# target_sentence = "yesterday when i went to my grandmother house i realized that she was so sick so i call my mother to come"
N = len(target_sentence)
char_size = len(chars)
population_size = 20
iterations = 1000
p_c = 0.3
p_m = 0.5
tournament_k = 3

# defining genetic necessary functions
def generate_random_genoum():
    genoum = []
    for i in range(N):
        index = np.random.randint(0,char_size)
        genoum.append(chars[index])
    return genoum

def cross_over(p1, p2):
    r = np.random.uniform(0,1)
    split_point = np.random.randint(0,N+1)
    p1_new = p2[0:split_point] + p1[split_point:N]
    p2_new = p1[0:split_point] + p2[split_point:N]
    return p1_new, p2_new

def mutation(c):
    r = np.random.uniform(0,1)
    if r > p_m:
        index = np.random.randint(0,N)
        char_index = np.random.randint(0,char_size)
        c[index] = chars[char_index]
    return c

def fitness_function(genome):
    cnt = 0
    for i in range(N):
        if target_sentence[i] == genome[i]:
            cnt += 1
    return cnt

def min_fitness_function(genome):
    cnt = N
    for i in range(N):
        if target_sentence[i] == genome[i]:
            cnt -= 1
    return cnt

def new_population_truncation_selection(children, old_population):
    # 20 of best genome go for the next population
    pairs = []
    new_population = []
    for i in range(population_size):
        pairs.append(tuple((i, fitness_function(children[i]))))
    for i in range(population_size):
        pairs.append(tuple((i+population_size, fitness_function(old_population[i]))))
    # increasing order
    pairs.sort(key=lambda tup: tup[1])
    for i in range(population_size):
        index = 2*population_size - 1
        pair = pairs[index]
        if pair[0] > 19:
            new_population.append(old_population[pair[0] - population_size])
        else:
            new_population.append(children[pair[0]])
    return new_population

def new_population_tournament_selection(children, old_population):
    combination_list = children + old_population
    x = len(combination_list)
    new_population = []
    cnt = 0
    while cnt < population_size:
        maxi = -1
        selected = None
        for i in range(tournament_k):
            index = np.random.randint(0, x)
            fit = fitness_function(combination_list[index])
            if fit > maxi:
                maxi = fit
                selected = combination_list[index]
        new_population.append(selected)
        cnt += 1
    return new_population

def genetic_algorithm(iteration):
    # creating the first population
    population = []
    for i in range(population_size):
        population.append(generate_random_genoum())

    for i in range(iteration):
        # choosing the parents randomly
        marks = [0 for i in range(population_size)]
        end_loop = 0
        children = []
        r1 = 0
        r2 = r1 + population_size - 1
        while r1 < r2:
            parent1 = population[r1]
            parent2 = population[r2]
            # cross over
            child1, child2 = cross_over(parent1, parent2)
            # mutation
            child1 = mutation(child1)
            child2 = mutation(child2)
            children.append(child1)
            children.append(child2)
            marks[r1] = 1
            marks[r2] = 1
            r2 -= 1
            r1 += 1
            end_loop = 1
            for i in range(population_size):
                end_loop = end_loop and marks[i]

        # ************ here the selecting the new population has different strategies ******************
        population = new_population_truncation_selection(children, population)
        # population = new_population_tournament_selection(children, population)
        # **********************************************************************************************

    return [''.join(x) for x in population]

# selecting the best answer from our last population
def select_the_best_genome_in_population(population):
    ans = None
    maxi = -1
    for i in range(population_size):
        genome = population[i]
        fit = fitness_function(genome)
        if fit > maxi:
            maxi = fit
            ans = genome
    return ans, maxi


p = genetic_algorithm(iterations)
print("---------- The Best Sentence That The Algorithm Has Created Is: ----------")
ans, max_fitness = select_the_best_genome_in_population(p)
print(ans)
print("maximum fitness is ",str(max_fitness)," out of ",str(N))