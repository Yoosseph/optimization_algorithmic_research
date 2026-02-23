# Genetic vs Trajectory — Job Shop Scheduling (JSSP)

This project compares **Genetic Algorithm (GA)** and **Trajectory‑based Hill Climbing (HC)** approaches on standard JSSP instances (e.g., `abz5`, `abz6`, `abz7`).  
It runs multiple trials, measures makespan and runtime, and produces convergence plots and distributions.

---

## Contents

- `genetic_algorithm/`
  - `genetic_algorithm.ipynb` — GA implementation + experiment runner
  - `genetic_docs.md` — GA function reference
- `trajectory_algorithm/`
  - `HC.ipynb` — Hill Climbing implementation + experiment runner
  - `trajectory_docs.md` — HC function reference
- `results/` — plots and summary outputs (if generated)

---

## Problem Overview (JSSP)

Each job has a fixed sequence of operations, each requiring a specific machine for a fixed duration.  
A valid schedule respects:
- **Job order**: operations must follow the given sequence
- **Machine capacity**: one job per machine at a time

**Goal:** minimize **makespan** (time to finish all jobs).

---

## Algorithms

### Genetic Algorithm (GA)
- **Representation:** chromosome is a list of job IDs; each job appears `num_machines` times
- **Fitness:** makespan computed by schedule simulation
- **Operators:**
  - Tournament selection
  - Order‑based crossover
  - Swap mutation
- **Extras:**
  - Adaptive mutation based on stagnation
  - Early stopping if no improvement

### Hill Climbing (HC)
- **Representation:** same chromosome format as GA
- **Move operators:**
  - `swap_adjacent`
  - `insert_move`
  - `reverse_segment`
- **Variants:**
  - Single HC
  - Random‑Restart HC
  - Per‑operator HC

---

## How to Run

### 1) Genetic Algorithm
Open and run the notebook:

- `genetic_algorithm/genetic_algorithm.ipynb`

This notebook:
- Runs GA on `abz5`, `abz6`, `abz7`
- Averages 25 runs per setting
- Plots convergence curves with best/avg/time per run

### 2) Hill Climbing
Open and run the notebook:

- `trajectory_algorithm/HC.ipynb`

This notebook:
- Runs Single HC and Random‑Restart HC
- Compares neighborhood operators
- Produces convergence plots + final distribution histograms

---

## Input Instances

Place instance files (`abz5.txt`, `abz6.txt`, `abz7.txt`, etc.) in the working directory where the notebooks are run.  
The parser expects the standard format:

```
<jobs> <machines>
<machine duration> <machine duration> ...
...
```

---

## Outputs

### GA Output
- Convergence plot per instance (avg of runs)
- Console summary: best, average, and runtime per run

### HC Output
- Two convergence plots per instance:
  - Single HC vs Random‑Restart HC
  - Per‑operator HC comparison
- Histogram of final makespan distribution

---

## Configuration

### GA Parameters (in notebook)
- `population_size`
- `generations`
- `mutation_rate`
- `elites`
- `adaptive_mutation` options

### HC Parameters (in notebook)
- `MAX_ITER`
- `RESTARTS`
- `N_RUNS`
- `HC_RR_RUNS`

---

## Notes

- Runs are stochastic; results vary by random seed.
- For fair comparisons, keep instance files and run counts consistent.
- Known optimum values are included for reference (e.g., `abz6 = 943`, `abz7 = 656`).

---

## References
- Standard JSSP benchmark instances: ABZ, FT, LA.