import random
import sys

def read_jobs(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    lines = [l.strip() for l in lines if l.strip()]
    num_jobs, num_machines = map(int, lines[0].split())
    jobs = []
    for i in range(1, num_jobs + 1):
        nums = list(map(int, lines[i].split()))
        ops = [(nums[j], nums[j+1]) for j in range(0, len(nums), 2)]
        jobs.append(ops)
    return jobs

def makespan(jobs, chrom):
    job_op = [0] * len(jobs)
    job_time = [0] * len(jobs)
    machine_time = [0] * len(jobs[0])
    for job in chrom:
        m, d = jobs[job][job_op[job]]
        start = max(job_time[job], machine_time[m])
        end = start + d
        job_time[job] = end
        machine_time[m] = end
        job_op[job] += 1
    return max(machine_time)

def random_chrom(num_jobs, num_machines):
    c = [j for j in range(num_jobs) for _ in range(num_machines)]
    random.shuffle(c)
    return c

def crossover(p1, p2):
    size = len(p1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[a:b] = p1[a:b]
    from collections import Counter
    placed = Counter(child[a:b])
    needed = Counter(p1)
    fill = []
    for g in p2[b:] + p2[:b]:
        if placed[g] < needed[g]:
            fill.append(g)
            placed[g] += 1
    pos = b % size
    for g in fill:
        while child[pos] is not None:
            pos = (pos + 1) % size
        child[pos] = g
        pos = (pos + 1) % size
    return child

def mutate(chrom):
    c = chrom[:]
    i, j = random.sample(range(len(c)), 2)
    c[i], c[j] = c[j], c[i]
    return c

def run(filename, mu=20, lam=100, generations=500, seed=42):
    random.seed(seed)
    jobs = read_jobs(filename)
    nj, nm = len(jobs), len(jobs[0])

    pop = sorted([random_chrom(nj, nm) for _ in range(mu)], key=lambda c: makespan(jobs, c))
    best = pop[0][:]
    best_ms = makespan(jobs, best)
    print(f"Gen 0 | Makespan: {best_ms}")

    for gen in range(1, generations + 1):
        offspring = []
        for _ in range(lam):
            p1 = random.choice(pop)
            p2 = random.choice(pop)
            child = crossover(p1, p2)
            child = mutate(child)
            offspring.append(child)

        pop = sorted(pop + offspring, key=lambda c: makespan(jobs, c))[:mu]

        ms = makespan(jobs, pop[0])
        if ms < best_ms:
            best_ms = ms
            best = pop[0][:]

        if gen % 50 == 0:
            print(f"Gen {gen} | Makespan: {best_ms}")

    print(f"\nBest makespan: {best_ms}")
    return best, best_ms

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    run(filename)