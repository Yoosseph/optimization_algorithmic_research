# Genetic Algorithm — Function Reference

## `parse_instance(file_path)`
- Reads a JSSP `.txt` instance.
- Extracts job count, machine count, and per‑job operation list.
- Returns: `(jobs, machines, jobs_data)`.

## `Individual`
- Simple container for a chromosome.
- Stores `chromosome` and computed `fitness`.

## `generate_chromosome(num_jobs, num_machines)`
- Builds a random chromosome.
- Each job appears `num_machines` times.
- Shuffles order and returns the list.

## `compute_makespan(chromosome, jobs_data)`
- Simulates the schedule implied by a chromosome.
- Tracks job and machine end times.
- Returns the final makespan (integer).

## `population_fitness_sort(population, jobs_data)`
- Computes fitness for each individual.
- Sorts population by best (lowest makespan).
- Returns sorted list.

## `tournament_selection(population, k=3)`
- Randomly samples `k` individuals.
- Returns the best (lowest fitness) among them.

## `crossover(parent1, parent2, num_jobs, num_machines)`
- Order‑based crossover for job counts.
- Preserves job multiplicities.
- Returns a new `Individual`.

## `mutate(individual, mutation_rate)`
- With probability `mutation_rate`, swaps two genes.
- Returns the (possibly) mutated individual.

## `genetic_algorithm(...)`
- Runs GA for one or more runs.
- Supports adaptive mutation and early stopping.
- Returns best individual and average makespan over runs.

## `run_ga_collect_curve(...)`
- Runs GA multiple times and records best‑per‑gen curves.
- Returns:
  - `avg_curve` (average best curve),
  - `avg_time_per_run`,
  - `run_times`,
  - `final_makespans`.