from abc import ABC, abstractmethod
from typing import TypedDict


class ShortResult(TypedDict):
    """Model the result of a shortest path execution"""
    shortestPath: list[Station] #type correct?
    nodesVisited: int


class ShortAlgorithm(ABC):

    __counter = 0

    def __call__(self, data: list[Station]) -> ShortResult:
        """Magic method to allow an object to be called as a function"""
        self.__counter = 0
        shallow = data.copy()
        result: ShortResult = {
            "sorted": self._sort(shallow),
            #how do i find the equivalent of build-in sort?
            "nodesVisited": self.__counter
        }
        return result

    def _incr(self, n=1):
        self.__counter += n

    @abstractmethod
    def _shortestPath(self, data: list[Station]) -> list[Station]: 
        #do we return the correct output? or is it just a print of the path.
        """Method that each algorithm must define"""
        pass
