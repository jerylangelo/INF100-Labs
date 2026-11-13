from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """Abstract base class for order discount strategy."""
    @abstractmethod
    def apply(self, total: float) -> float:
        """Abstract method to apply a discount to the given order total"""
        pass


