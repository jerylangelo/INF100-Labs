from DiscountStrategy import DiscountStrategy


class StudentDiscount(DiscountStrategy):
    """Custom strategy applying a student 5% discount"""
    
    def __init__(self, percentage: float = 5.0) -> None:
        self.percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1.0 - (self.percentage / 100.0))