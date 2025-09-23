from dataclasses import dataclass, field
from typing import List, Optional
from .Corrida import Corrida

@dataclass
class Motorista:
    nome: str
    documento: str
    corridas: List[Corrida] = field(default_factory=list)
    nota: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "nome": self.nome,
            "documento": self.documento,
            "corridas": [c.to_dict() for c in self.corridas],
            "nota": int(self.nota) if self.nota is not None else None
        }

    @staticmethod
    def from_dict(d: dict) -> "Motorista":
        corridas = [Corrida.from_dict(c) for c in d.get("corridas", [])]
        return Motorista(
            nome=d.get("nome", ""),
            documento=d.get("documento", ""),
            corridas=corridas,
            nota=d.get("nota", None)
        )
