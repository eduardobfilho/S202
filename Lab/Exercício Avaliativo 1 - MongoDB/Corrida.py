from dataclasses import dataclass
from .Passageiro import Passageiro

@dataclass
class Corrida:
    nota: int
    distancia: float
    valor: float
    passageiro: Passageiro

    def to_dict(self) -> dict:
        return {
            "nota": int(self.nota),
            "distancia": float(self.distancia),
            "valor": float(self.valor),
            "passageiro": self.passageiro.to_dict()
        }

    @staticmethod
    def from_dict(d: dict) -> "Corrida":
        p = Passageiro.from_dict(d.get("passageiro", {}))
        return Corrida(
            nota=int(d.get("nota", 0)),
            distancia=float(d.get("distancia", 0.0)),
            valor=float(d.get("valor", 0.0)),
            passageiro=p
        )
