class Module:
    """Base class for all neural network modules"""

    def __init__(self):
        self._parameters = {}
        self._modules = {}

    def forward(self, *args, **kwargs):
        """Forward pass of the module"""
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
