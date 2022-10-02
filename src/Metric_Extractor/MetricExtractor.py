import Strategy
import Metric
from OutputHelpers import output_helper, prettyOutput


class MetricExtractor():

    start_node = None
    target_node = None
    pathList = []
    infoList = []
    _strategy = None
    _metric = None
    threshold = 0

    def __init__(self, graph) -> None:
        self.graph = graph

    # set property for algorithm
    @property
    def strategy(self) -> Strategy:
        return self._strategy

    # set property for metric
    @property
    def metric(self) -> Metric:
        return self._metric

    # set algorithm to analyze
    @strategy.setter
    def setStrategy(self, strategy) -> None:
        self._strategy = strategy

    # set metric to compute
    @metric.setter
    def setMetric(self, metric) -> None:
        self._metric = metric

    # method to use metric's abstract method to
    # compute metric
    def compute_metric(self, metric) -> None:
        self._metric = metric
        result = self._metric.compute_metric(self.graph)
        return result

    # method to use algorithms's abstract method to
    # compute metric
    def algorithm(self, start_node, target_node) -> None:
        self.start_node = start_node
        self.target_node = target_node

        result = self._strategy.do_algorithm(
            self.graph, start_node, target_node)
        self.pathList = result

        # if nodes are equivalent then return
        if start_node == target_node:
            print("You're already here!")
        else:
            return result

    # set threshold for algorithm path traversal
    def set_threshold(self, threshold) -> None:
        self.threshold = threshold

    # use helper functions to format output
    def print_output(self):
        result = output_helper(self.graph, self.pathList, self.threshold)
        self.infoList = result

        if len(result) == 0:
            print("You're already here!")
        else:
            prettyOutput(result)
