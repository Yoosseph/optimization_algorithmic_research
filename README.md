# Optimization Algorithmic Research

This repository is a collection of optimization experiments built around notebooks and benchmark data files.  
The main idea is to compare different algorithmic approaches on routing, scheduling, and multi objective problems.

## How the repository works

The project is split into three folders.

1. `SPEA_vs_NSGA`  
This part focuses on multi objective optimization work and includes the main notebook `MOOA_1.ipynb` with supporting data files.

2. `genetic_vs_trajectory`  
This part compares a genetic approach with a trajectory based local search approach for job shop scheduling.  
It includes algorithm notebooks, input instances, and generated result plots.

3. `solving_routing_problems`  
This part contains routing experiments and notebooks with CVRP and VRPTW style input files.

## How to run things

1. Open the folder you want to work on.  
2. Start Jupyter and run the notebook in that folder from top to bottom.  
3. Keep each `.txt` instance file in the same working location expected by the notebook.  
4. Save outputs or plots in the existing folder structure.

## Notes

Most of the work here is experiment driven, so outputs can vary between runs when randomness is involved.  
If you want fair comparisons, keep the same instances and run settings when testing different algorithms.
