from abc import ABC, abstractmethod


class Metric(ABC):

    @abstractmethod
    def compute_metric(self, graph):
        pass
