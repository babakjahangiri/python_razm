import abc
from abc import abstractmethod


class ProductSave(abc.ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def read_by_title(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def list_all(self):
        pass

