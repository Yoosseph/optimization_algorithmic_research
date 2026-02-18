# Hill Climbing — Function Reference

## `parse_instance(file_path)`
- Reads a JSSP `.txt` instance.
- Extracts job count, machine count, and per‑job operation list.
- Returns: `(jobs, machines, jobs_data)`.

## `makespan(chromosome, jobs, n_machines)`
- Simulates the schedule implied by a chromosome.
- Tracks job and machine end times.
- Returns `(best_makespan, schedule)`.

## `random_chromosome(n_jobs, n_machines)`
- Builds a random chromosome.
- Each job appears `n_machines` times.
- Returns the shuffled list.

## `swap_adjacent(chrom)`
- Swaps two adjacent genes at a random index.
- Returns the new chromosome.

## `insert_move(chrom)`
- Removes one gene and inserts it at a new index.
- Returns the new chromosome.

## `reverse_segment(chrom)`
- Reverses a random segment of the chromosome.
- Returns the new chromosome.

## `hill_climbing(jobs, n_jobs, n_machines, max_iter=..., operator=None)`
- Core HC loop.
- Replaces current solution when a neighbor is not worse.
- Returns `(best_chromosome, best_makespan, history)`.

## `random_restart_hill_climbing(jobs, n_jobs, n_machines, max_iter=..., n_restarts=...)`
- Runs HC multiple times with different random starts.
- Keeps the best solution.
- Returns `(best_chromosome, best_makespan, full_history)`.

## `run_hc_suite(file_path, label)`
- Runs Single HC and Random‑Restart HC (with averages).
- Runs per‑operator HC and plots convergence.
- Prints summary stats and plots distribution.