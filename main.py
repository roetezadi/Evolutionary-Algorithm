import numpy as np

def fitness(a):
    y = a[0]*2 + a[1] + a[2]*3
    return np.abs(y - 19)

def crossover(a, b):
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    b1 = b[0]
    b2 = b[1]
    b3 = b[2]
    aa = [b2, b3, a1]
    bb = [a2, a3, b1]
    return aa, bb

population = []
for i in range(6):
    x = np.random.randint(0, 5)
    y = np.random.randint(0, 5)
    z = np.random.randint(0, 5)
    population.append([x, y, z])

# population = np.array(population)

for i in range(1000):
    index1 = np.random.randint(0, len(population))
    index2 = np.random.randint(0, len(population))
    p1, p2 = crossover(population[index1], population[index2])
    population.append(p1)
    population.append(p2)

mini = 1000
ans = 0
for i in range(len(population)):
    fit1 = fitness(population[i])
    if fit1 < mini:
        mini = fit1
        ans = population[i]
print(mini)
print(ans)