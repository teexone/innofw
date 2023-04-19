import torch
from abc import ABC, abstractmethod

class ImageToText(torch.nn.Module, ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    @abstractmethod
    def initialize():
        pass