from DiscountStrategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    """Strategy that applies a fixed discount if the total meets or exceeds a threshold"""
    
    def __init__(self, threshold: float, discount_amount: float) -> None:
        self.threshold: float = threshold
        self.discount_amount: float = discount_amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.discount_amount
        return total