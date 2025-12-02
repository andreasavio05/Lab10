import datetime
from dataclasses import dataclass


class Spedizione:
    def __init__(self, hub1, hub2, peso):
        self.hub1 = hub1
        self.hub2 = hub2
        self.peso = peso

    def __eq__(self, other):
        return isinstance(other, Spedizione) and self.id == other.id

    def __str__(self):
        return f"{self.numero_tracking}"

    def __repr__(self):
        return f"{self.numero_tracking}"


