class Scalar:
    """Class for scalar autograd operations"""

    def __init__(self, data, requires_grad=False):
        self.data = data
        self.grad = None
        self.requires_grad = requires_grad

    def backward(self):
        """Compute gradients"""
        if not self.requires_grad:
            return
        self.grad = 1.0
