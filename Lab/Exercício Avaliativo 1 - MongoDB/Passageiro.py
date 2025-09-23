from dataclasses import dataclass, asdict

@dataclass
class Passageiro:
    nome: str
    documento: str

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: dict) -> "Passageiro":
        return Passageiro(
            nome=d.get("nome", ""),
            documento=d.get("documento", "")
        )
