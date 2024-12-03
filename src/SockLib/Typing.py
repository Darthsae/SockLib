from typing import Protocol, runtime_checkable

@runtime_checkable
class SupportsAddition(Protocol):
    def __add__(self, other):
        pass

@runtime_checkable
class SupportsSubtraction(Protocol):
    def __sub__(self, other):
        pass

@runtime_checkable
class SupportsMultiplication(Protocol):
    def __mul__(self, other):
        pass

@runtime_checkable
class SupportsDivision(Protocol):
    def __div__(self, other):
        pass

@runtime_checkable
class SupportsAverage(Protocol):
    def __radd__(self, other):
        pass
    
    def __add__(self, other):
        pass
    
    def __div__(self, other):
        pass