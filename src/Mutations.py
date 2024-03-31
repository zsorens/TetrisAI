import random
#function for swap mutation
def swap_mutation(path, moveCounter):
    mutated_path = path                                #copy the original path
    idx1, idx2 = random.sample(range(moveCounter), 2)             #randomly select two indices for swap
    mutated_path[idx1], mutated_path[idx2] = mutated_path[idx2], mutated_path[idx1]  #swap the selected indices
    return mutated_path   

#function for inversion mutation
def inversion_mutation(path, moveCounter):
    mutated_path = path                                 #copy the original path
    start_idx = random.randint(0, moveCounter - 1)                #randomly select a starting index
    end_idx = random.randint(start_idx, moveCounter - 1)          #randomly select an ending index
    mutated_path[start_idx:end_idx + 1] = reversed(mutated_path[start_idx:end_idx + 1]) #reverse the sublist from starting index to ending index
    return mutated_path  

#function for ordered crossover
def ordered_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)  
    child1 = parent1[:crossover_point] + parent2[crossover_point:]  #take the first part of parent 1 until crossover, then fill in from parent 2
    child2 = parent2[:crossover_point] + parent1[crossover_point:]  #reverse for child 2
    # child1 = parent1[] + [city for city in parent2 if city not in parent1[crossover_point]]  #take the first part of parent 1 until crossover, then fill in from parent 2
    # child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]  #reverse for child 2
    return child1, child2

#function for cycle crossover
def cycle_crossover(parent1, parent2):
    cycle_start = random.randint(0, len(parent1.moves) - 1)           #randomly select a starting city for the cycle
    child1, child2 = [-1] * len(parent1.moves), [-1] * len(parent2.moves)   #initialize child paths
    while True:
        child1[cycle_start] = parent1[cycle_start]              #mark current city in child 1
        child2[cycle_start] = parent2[cycle_start]              #mark current city in child 2
        cycle_start = parent2.index(parent1[cycle_start])       #find the corresponding city from parent 2
        if child1[cycle_start] != -1:                           #if cycle is done break
            break
    for i in range(len(parent1)):                               #fill the remaining cities using the parents
        if child1[i] == -1:
            child1[i] = parent2[i]                              #child1 with parent 2
            child2[i] = parent1[i]                              #child2 with parent 1
    return child1, child2

def cycle_crossover1(parent1, parent2):
    length = len(parent1)
    child1 = [-1] * length
    child2 = [-1] * length

    # Create a cycle
    cycle_start = parent1[0]
    while True:
        index = parent1.index(cycle_start)
        child1[index] = parent1[index]
        child2[index] = parent2[index]

        if parent1[index] == parent2[index]:
            break

    # Fill in the remaining positions in the child
    for i in range(length):
        if child1[i] == -1:
            child1[i] = parent2[i]
            child2[i] = parent1[i]

    return child1, child2

def custom_crossover(parent1, parent2):
    length = len(parent1)
    start, end = sorted(random.sample(range(length), 2))

    # Create children with genetic material between start and end from the first parent
    child1 = [None] * length
    child1[start:end] = parent1[start:end]

    child2 = [None] * length
    child2[start:end] = parent2[start:end]

    # Fill in the remaining positions in the children with genetic material from the second parent
    index_child1 = end
    index_child2 = end

    while None in child1:
        if parent2[index_child2 % length] not in child1:
            child1[index_child1 % length] = parent2[index_child2 % length]
            index_child1 += 1
        index_child2 += 1

    while None in child2:
        if parent1[index_child1 % length] not in child2:
            child2[index_child2 % length] = parent1[index_child1 % length]
            index_child2 += 1
        index_child1 += 1

    return child1, child2

def point_crossover(parent1, parent2, moveCounter):
    length = len(parent1)
    crossover_point = random.randint(0, moveCounter)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2