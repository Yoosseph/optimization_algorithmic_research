# Hill Climbing — Function Reference (Expanded)

## `parse_instance(file_path)`
Reads a JSSP `.txt` instance and parses the problem data.  
It finds the `jobs machines` line, then reads each job’s operations as `(machine, duration)` pairs.  
**Returns:** `(jobs, machines, jobs_data)`.

**Example (conceptual):**  
If the file starts with `3 2`, it returns 3 jobs, 2 machines, and a list of 3 jobs, each with 2 operations.

---

## `makespan(chromosome, jobs, n_machines)`
Simulates the schedule encoded by the chromosome.  
Each gene is a job ID; the function schedules that job’s **next operation** when both the job and its machine are free.  
It tracks job and machine end times and returns the **final completion time** (makespan) and a per‑machine schedule.

**Example (conceptual):**  
If the chromosome starts `[0,1,0,1]`, it schedules job 0’s first op, then job 1’s first op, then job 0’s second op, and so on, respecting machine availability.

---

## `random_chromosome(n_jobs, n_machines)`
Creates a random chromosome where each job appears exactly `n_machines` times.  
This ensures the chromosome length is `n_jobs * n_machines`.

**Example:**  
`n_jobs=3, n_machines=2` → a shuffled list like `[1,0,2,1,0,2]`.

---

## `swap_adjacent(chrom)`
Neighbourhood operator that swaps two adjacent genes at a random position.  
This makes a small, local change to the schedule.

**Example:**  
`[0,1,2,0]` → swap at index 1 gives `[0,2,1,0]`.

---

## `insert_move(chrom)`
Neighbourhood operator that removes one gene and inserts it at another index.  
This can produce a larger rearrangement than a swap.

**Example:**  
`[0,1,2,0]` → move index 0 to index 2 gives `[1,2,0,0]`.

---

## `reverse_segment(chrom)`
Neighbourhood operator that reverses a random segment of the chromosome.  
This changes the relative order of several operations at once.

**Example:**  
`[0,1,2,0,1]` → reverse positions 1–3 gives `[0,0,2,1,1]`.

---

## `hill_climbing(jobs, n_jobs, n_machines, max_iter=..., operator=None)`
Core hill‑climbing loop.  
Starts from a random chromosome and repeatedly accepts a neighbour if it is **not worse** (lower or equal makespan).  
Returns the best chromosome found, its makespan, and the convergence history.

**Example:**  
Over iterations, the makespan typically drops quickly and then plateaus.

---

## `random_restart_hill_climbing(jobs, n_jobs, n_machines, max_iter=..., n_restarts=...)`
Runs hill climbing multiple times from different random starts.  
Keeps the best solution across all restarts and concatenates histories.

**Example:**  
If one restart gets stuck in a local optimum, another restart can find a better one.

---

## `run_hc_suite(file_path, label)`
End‑to‑end experiment runner.  
It runs **Single HC** and **Random‑Restart HC**, plus per‑operator HC, and plots convergence curves.  
It also prints summary stats and shows a distribution of final makespans.

**Example:**  
Produces two convergence plots and a histogram for each instance.