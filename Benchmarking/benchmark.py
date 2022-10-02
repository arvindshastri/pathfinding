import pyperf
import random
import sys

import GraphBuilder ##need to sys
sys.path.insert(0,'./../src') #correct?
from src import GraphBuilder #idk

from factory import ShortestFactory
from interface import ShortAlgorithm


def main():
    """Running the complete benchmark"""
    random.seed(1) #argument matters? idk
    random_nodes = gen_nodes()
    algorithms = ['a*', 'dijkstra']
    
    do_bench(algorithms, random_nodes)


def gen_nodes() -> list[Station]:
    """generate a list of two random station objects"""
    stations=GraphBuilder.getStationsDict().values() #syntax
    upper_bound = len(stations) - 1
    i=random.randint(0,upper_bound)
    j=random.randint(0,upper_bound)
    return [stations[i],stations[j]]



def do_bench(algorithms: list[ShortAlgorithm], nodes: list[Station]) -> None:
    """run the benchmark over a set of algorithm"""
    runner = pyperf.Runner()
    for algorithm in algorithms:
        pathfinder = ShortestFactory.build(algorithm)
        runner.bench_func(algorithm, pathfinder, nodes)


if __name__ == "__main__":
    main()
#??