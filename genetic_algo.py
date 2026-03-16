#!/usr/bin/env python3
"""Genetic algorithm framework — selection, crossover, mutation."""
import random, sys

class GA:
    def __init__(self, pop_size=50, gene_len=20, mut_rate=0.02):
        self.pop_size=pop_size; self.gene_len=gene_len; self.mut_rate=mut_rate
        self.pop=[[random.randint(0,1) for _ in range(gene_len)] for _ in range(pop_size)]
    def fitness(self, ind): return sum(ind)
    def select(self):
        t = random.sample(self.pop, 3)
        return max(t, key=self.fitness)
    def crossover(self, a, b):
        pt = random.randint(1, self.gene_len-1)
        return a[:pt]+b[pt:], b[:pt]+a[pt:]
    def mutate(self, ind):
        return [1-g if random.random()<self.mut_rate else g for g in ind]
    def evolve(self, generations=100):
        for gen in range(generations):
            new_pop = []
            best = max(self.pop, key=self.fitness)
            new_pop.append(best)
            while len(new_pop) < self.pop_size:
                p1, p2 = self.select(), self.select()
                c1, c2 = self.crossover(p1, p2)
                new_pop.extend([self.mutate(c1), self.mutate(c2)])
            self.pop = new_pop[:self.pop_size]
            if gen % (generations//5) == 0:
                print(f"Gen {gen:3d}: best={self.fitness(best)}/{self.gene_len}")
        return max(self.pop, key=self.fitness)

if __name__ == "__main__":
    random.seed(42)
    ga = GA(pop_size=50, gene_len=30)
    best = ga.evolve(100)
    print(f"Final: {sum(best)}/{len(best)} ones")
