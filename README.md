# Genetic Algorithm for String Matching
In this project I try to use genetic algorithm to find a sentence from random genoms to match a target sentence.

The algorithm is based on the basic genetic algorithms:

### Representation: 
There is a list of size N (number of characters in the target sentence). each item in the list is a character. There are other representations such as using ASCII codes for each character so that there will be binary genomes. 

### Crossover: 
Using 1-point crossover - The split point is random.

### Mutation: 
For each genome, a random index of it is chosen and it will be replaced by a random character from the character list.

### Fitness Function:
The fitness function returns an integer number which is the number of correct character that the genome has.

### Population: 
Population size is 20 chromosomes. In the first iteration 20 random chromosomes with the size of 20 will be generated. In each iteration two method of population selection is used (truncated and tournament). The value of K for the tournament method is 3.



# The final answer in this algorithm is highly dependent on the total iteration and the target sentence length. If the size of the target sentence is high then the iteration size should be increased. 
