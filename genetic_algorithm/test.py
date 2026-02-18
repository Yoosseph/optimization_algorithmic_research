import random
from time import time


# =========================
# ===== DATA PARSING ======
# =========================

def parse_instance(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    # Find line with "jobs machines"
    for i, line in enumerate(lines):
        if line[0].isdigit():
            jobs, machines = map(int, line.split())
            start_index = i + 1
            break

    jobs_data = []

    for line in lines[start_index:start_index + jobs]:
        numbers = list(map(int, line.split()))
        operations = []
        for i in range(0, len(numbers), 2):
            machine = numbers[i]
            duration = numbers[i + 1]
            operations.append((machine, duration))
        jobs_data.append(operations)

    return jobs, machines, jobs_data


# =========================
# ===== REPRESENTATION ====
# =========================

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None


def generate_chromosome(num_jobs, num_machines):
    chromosome = []
    for job in range(num_jobs):
        chromosome += [job] * num_machines
    random.shuffle(chromosome)
    return chromosome


# =========================
# ===== MAKESPAN ==========
# =========================

def compute_makespan(chromosome, jobs_data):
    num_jobs = len(jobs_data)
    num_machines = len(jobs_data[0])

    job_next_op = [0] * num_jobs
    job_end_time = [0] * num_jobs
    machine_end_time = [0] * num_machines

    for job in chromosome:
        op_index = job_next_op[job]
        machine, duration = jobs_data[job][op_index]

        start_time = max(job_end_time[job], machine_end_time[machine])
        end_time = start_time + duration

        job_end_time[job] = end_time
        machine_end_time[machine] = end_time
        job_next_op[job] += 1

    return max(job_end_time)


# =========================
# ===== FITNESS ===========
# =========================

def evaluate_population(population, jobs_data):
    for ind in population:
        ind.fitness = compute_makespan(ind.chromosome, jobs_data)

    population.sort(key=lambda x: x.fitness)
    return population


# =========================
# ===== SELECTION =========
# =========================

def tournament_selection(population, k=3):
    contenders = random.sample(population, k)
    contenders.sort(key=lambda x: x.fitness)
    return contenders[0]


# =========================
# ===== CROSSOVER =========
# =========================

def crossover(parent1, parent2, num_jobs, num_machines):
    size = len(parent1.chromosome)

    a, b = sorted(random.sample(range(size), 2))

    child = [None] * size
    child[a:b] = parent1.chromosome[a:b]

    required_count = {job: num_machines for job in range(num_jobs)}

    for gene in child[a:b]:
        required_count[gene] -= 1

    fill_index = 0
    for gene in parent2.chromosome:
        if required_count[gene] > 0:
            while child[fill_index] is not None:
                fill_index += 1
            child[fill_index] = gene
            required_count[gene] -= 1

    return Individual(child)


# =========================
# ===== MUTATION ==========
# =========================

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual.chromosome)), 2)
        individual.chromosome[i], individual.chromosome[j] = \
            individual.chromosome[j], individual.chromosome[i]
    return individual


# =========================
# ===== GENETIC ALG =======
# =========================

def genetic_algorithm(file_path,
                      population_size=100,
                      generations=200,
                      mutation_rate=0.1,
                      elites=2):

    num_jobs, num_machines, jobs_data = parse_instance(file_path)

    population = [
        Individual(generate_chromosome(num_jobs, num_machines))
        for _ in range(population_size)
    ]

    best_overall = None

    for gen in range(generations):

        population = evaluate_population(population, jobs_data)

        if best_overall is None or population[0].fitness < best_overall.fitness:
            best_overall = population[0]

        print(f"Generation {gen} | Best makespan: {population[0].fitness}")

        new_population = population[:elites]

        while len(new_population) < population_size:
            p1 = tournament_selection(population)
            p2 = tournament_selection(population)

            child = crossover(p1, p2, num_jobs, num_machines)
            child = mutate(child, mutation_rate)

            new_population.append(child)

        population = new_population

    print("\nBest solution found:")
    print("Makespan:", best_overall.fitness)
    return best_overall


# =========================
# ===== RUN EXAMPLE =======
# =========================

if __name__ == "__main__":
    # Replace with your instance file path
    best = genetic_algorithm("abz5.txt",
                             population_size=100,
                             generations=200,
                             mutation_rate=0.1,
                             elites=2)
