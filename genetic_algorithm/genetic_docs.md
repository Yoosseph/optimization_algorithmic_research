# Genetic Algorithm — Function Reference (Expanded)

## `parse_instance(file_path)`
Reads a JSSP text file and parses the problem data.  
It finds the line with `jobs machines`, then reads each job’s operations as `(machine, duration)` pairs.  
**Returns:** `(jobs, machines, jobs_data)`.

**Example (conceptual):**  
If the file starts with `3 2`, the function returns 3 jobs, 2 machines, and a list of 3 jobs, each with 2 operations.

---

## `Individual`
A small container class that holds a chromosome and its fitness value.  
Fitness is filled in later by evaluation functions.

**Example:**  
`Individual([0,1,2,0,1,2])` stores the order of job operations; `fitness` will be set after evaluation.

---

## `generate_chromosome(num_jobs, num_machines)`
Creates a random chromosome where each job appears exactly `num_machines` times.  
This guarantees the chromosome length equals `num_jobs * num_machines`.

**Example:**  
`num_jobs=3, num_machines=2` → a shuffled list like `[1,0,2,1,0,2]`.

---

## `compute_makespan(chromosome, jobs_data)`
Simulates the schedule encoded by the chromosome.  
Each gene is a job ID; the function schedules that job’s **next operation** when its job and required machine are both free.  
It tracks end times for each job and machine, then returns the latest finish time (the makespan).

**Example (conceptual):**  
If the chromosome starts `[0,1,0,1]`, Job 0’s first op is scheduled, then Job 1’s first op, then Job 0’s second op, and so on, always respecting machine and job availability.

---

## `population_fitness_sort(population, jobs_data)`
Evaluates fitness (makespan) for every individual.  
Then sorts the list so the best (lowest makespan) is first.

**Example:**  
After sorting, `population[0]` is the current best solution.

---

## `tournament_selection(population, k=3)`
Randomly samples `k` individuals and returns the best among them.  
This balances randomness with selection pressure.

**Example:**  
If 3 candidates are picked, the one with the lowest makespan is chosen.

---

## `crossover(parent1, parent2, num_jobs, num_machines)`
Order‑based crossover:  
- Copy a random slice from `parent1`.  
- Fill remaining positions with genes from `parent2` while keeping correct job counts.

**Example:**  
The child keeps a segment from `parent1`, then fills the rest from `parent2` without duplicating job counts.

---

## `mutate(individual, mutation_rate)`
With probability `mutation_rate`, swaps two random genes.  
This introduces diversity and helps escape local optima.

**Example:**  
`[0,1,2,0,1,2]` might become `[0,2,1,0,1,2]`.

---

## `genetic_algorithm(...)`
Main GA loop.  
It initializes a population, evaluates fitness, selects parents, applies crossover and mutation, and repeats for many generations.  
Supports adaptive mutation and early stopping.

**Example:**  
Returns the best individual found and the average makespan across runs.

---

## `run_ga_collect_curve(...)`
Runs GA multiple times and records the best value at each generation.  
Computes an average curve and average runtime per run.

**Returns:**  
- `avg_curve` (average best‑per‑gen),  
- `avg_time_per_run`,  
- `run_times`,  
- `final_makespans`.