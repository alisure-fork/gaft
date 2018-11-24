"""
Find the global maximum for binary function: f(x) = y*sim(2*pi*x) + x*cos(2*pi*y)
"""
import math
from gaft import GAEngine
from gaft.components import BinaryIndividual
from gaft.components import Population
from gaft.operators import TournamentSelection
from gaft.operators import UniformCrossover
from gaft.operators import FlipBitBigMutation
from gaft.analysis.fitness_store import FitnessStore
from gaft.analysis.console_output import ConsoleOutput


individual_template = BinaryIndividual(ranges=[(-2, 2), (-2, 2)], eps=0.001)
population = Population(indv_template=individual_template, size=50).init()


selection = TournamentSelection()
crossover = UniformCrossover(pc=0.8, pe=0.5)
mutation = FlipBitBigMutation(pm=0.1, pbm=0.55, alpha=0.6)


engine = GAEngine(population=population, selection=selection,
                  crossover=crossover, mutation=mutation, analysis=[ConsoleOutput, FitnessStore])


@engine.fitness_register
def fitness(individual):
    x, y = individual.solution
    return y * math.sin(2 * math.pi * x) + x * math.cos(2 * math.pi * y)


if '__main__' == __name__:
    engine.run(ng=100)
