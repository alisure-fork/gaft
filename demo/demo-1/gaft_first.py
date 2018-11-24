from gaft import GAEngine
from gaft.components import BinaryIndividual  # 二元个体
from gaft.components import Population  # 人口
from gaft.operators import RouletteWheelSelection  # 轮盘选择
from gaft.operators import UniformCrossover  # 均匀交叉
from gaft.operators import FlipBitMutation  # 翻转突变

from gaft.analysis.fitness_store import FitnessStore
from gaft.analysis.console_output import ConsoleOutput
from gaft.plugin_interfaces.analysis import OnTheFlyAnalysis  # 瞬时分析

import math

# 定义编码
individual_template = BinaryIndividual(ranges=[(0, 10)], eps=0.001)

# 定义种群
_population = Population(indv_template=individual_template, size=20)

# 种群初始化
_population.init()

# 遗传操作
selection = RouletteWheelSelection()  # 个体选择:轮盘赌
crossover = UniformCrossover(pc=0.8, pe=0.5)  # 交叉算子:均匀交叉
mutation = FlipBitMutation(pm=0.1)  # 变异算子:翻转突变

# 遗传算法引擎
_engine = GAEngine(population=_population, selection=selection,
                   crossover=crossover, mutation=mutation, analysis=[FitnessStore, ConsoleOutput])


# 适应度：目标
@_engine.fitness_register
# @_engine.minimize
def fitness(individual):
    x, = individual.solution
    return 0.01 * x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)


@_engine.analysis_register
class ConsoleOutputAnalysis(OnTheFlyAnalysis):

    def setup(self, ng, engine):

        pass

    master_only = True
    interval = 1

    def register_step(self, g, population, engine):
        population.best_indv(engine.fitness)
        msg = 'Generation: {}, best fitness: {:.3f}'.format(g, engine.fmax)
        engine.logger.info(msg)

    def finalize(self, population, engine):
        best_individual = population.best_indv(engine.fitness)
        x = best_individual.solution
        y = engine.ori_fmax

        msg = 'Optimal solution: ({}, {})'.format(x, y)
        self.logger.info(msg)
        pass


if __name__ == '__main__':
    _engine.run(ng=10)
