# GA
In this project I try to use genetic algorithm to find a sentence from random genoms to match the target sentence

The algorithm is based on the basic genetic algorithms:

### representation: 
there is a list of size N (number of characters in the target sentence). each item in the list is a character.

### crossover: 
using 1-point crossover - the split point is random

### mutation: 
each genome a random index of the genome is chosen and it will be replaced by a random character

### fitness:
the fitness function returns the number of correct character the genome has (higher the fitness better the genome for next generation:))

### population: 
population size is 20 genome and in each iteration two method of population selection is used (truncated and tournament)
