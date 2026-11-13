
from DiscountStrategy import DiscountStrategy


class NoDiscount(DiscountStrategy):
    """Strategy that leaves the order total unchanged"""
    
    def apply(self, total: float) -> float:
        return total