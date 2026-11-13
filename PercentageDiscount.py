from DiscountStrategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    """Strategy that applies a percentage-based discount"""
    
    def __init__(self, percentage: float) -> None:
        self.percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1.0 - (self.percentage / 100.0))