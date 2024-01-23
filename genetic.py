import random

def chromosomeGenerator(list):
    for i in range(10):
        list.append(random.randint(0, 1))
    
    return list

def populationGenerator(population):
    for i in range(20):
        list=[]
        population.append(chromosomeGenerator(list))
    return population

def crossover(chromosome1, chromosome2):
    child1 = chromosome1[0:5] + chromosome2[5:10]
    child2 = chromosome2[0:5] + chromosome1[5:10]
    return [child1, child2]

def mutation(chromosome):
    probability = 0.05
    cond = random.random()

    if cond < probability:
        index = random.randint(0,9)
        print("Condition", cond)
        print("Original Chromosome", chromosome)
        chromosome[index] = chromosome[index] ^ 1
        print("Mutated chromosome", chromosome)
        return chromosome


def generationGenerator(population):
    

    for i in range(3):
        
        childpopulation = []
        print("\n\n-----------------------------------------")
        print("Population:", i)
        print("-----------------------------------------\n\n")
        for i in range(10):
            chromosome1 = population[i * 2]
            chromosome2 = population[i * 2 + 1]
            (child1, child2) = (crossover(chromosome1, chromosome2))
            childpopulation.append(child1)
            childpopulation.append(child2)

        print("Child population", *childpopulation, sep='\n')

        for i in range(len(childpopulation)):
            mutation(childpopulation[i])

        print("Mutated Child", *childpopulation, sep='\n')



def main():
    population = []
    population = populationGenerator(population)
    print("Parent Population: ", population)
    print("----------------------------------------------------")
    generationGenerator(population)



main()
