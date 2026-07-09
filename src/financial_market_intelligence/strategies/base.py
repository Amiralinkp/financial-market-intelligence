from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    @abstractmethod
    def generate_signal(self, data):
        pass

    @abstractmethod
    def get_name(self):
        pass

    def get_parameters(self):
        pass

    def get_required_indicators(self):
        raise NotImplementedError