class Tensor:
    """Base tensor class for kiwitorch"""

    def __init__(self, data):
        self.data = data
        self.grad = None
        self.requires_grad = False

    def backward(self):
        """Compute gradients through backpropagation"""
