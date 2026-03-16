import random
class GA:
    def __init__(s, pop_size=50, gene_length=10, fitness_fn=None, mutation_rate=0.01):
        s.pop_size=pop_size; s.gene_length=gene_length; s.mutation_rate=mutation_rate
        s.fitness_fn=fitness_fn or (lambda g: sum(g))
        s.population=[[random.randint(0,1) for _ in range(gene_length)] for _ in range(pop_size)]
    def fitness(s, individual): return s.fitness_fn(individual)
    def select(s):
        tournament = random.sample(s.population, min(5, len(s.population)))
        return max(tournament, key=s.fitness)
    def crossover(s, p1, p2):
        pt = random.randint(1, len(p1)-1)
        return p1[:pt]+p2[pt:], p2[:pt]+p1[pt:]
    def mutate(s, individual):
        return [1-g if random.random()<s.mutation_rate else g for g in individual]
    def evolve(s, generations=100):
        best_history = []
        for gen in range(generations):
            new_pop = []
            for _ in range(s.pop_size//2):
                p1, p2 = s.select(), s.select()
                c1, c2 = s.crossover(p1, p2)
                new_pop.extend([s.mutate(c1), s.mutate(c2)])
            s.population = new_pop[:s.pop_size]
            best = max(s.population, key=s.fitness)
            best_history.append(s.fitness(best))
        return max(s.population, key=s.fitness), best_history
def demo():
    random.seed(42)
    ga = GA(pop_size=100, gene_length=20, fitness_fn=lambda g: sum(g), mutation_rate=0.02)
    best, history = ga.evolve(50)
    print(f"Best: {best} fitness={sum(best)}")
    print(f"Progress: gen0={history[0]}, gen25={history[25]}, gen49={history[49]}")
if __name__ == "__main__": demo()
