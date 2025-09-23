from bson.objectid import ObjectId
from Motorista import Motorista
from Corrida import Corrida

class MotoristaDAO:
    def __init__(self, database, collection_name="Motoristas"):
        self.db = database
        self.col = self.db.collection(collection_name)

    def create_motorista(self, motorista: Motorista) -> str:
        doc = {k: v for k, v in motorista.to_dict().items() if v is not None}
        result = self.col.insert_one(doc)
        return str(result.inserted_id)

    def list_motoristas(self):
        return list(self.col.find())

    def get_motorista(self, id_str: str):
        try:
            _id = ObjectId(id_str)
        except Exception:
            return None
        return self.col.find_one({"_id": _id})

    def update_motorista(self, id_str: str, update_fields: dict) -> bool:
        try:
            _id = ObjectId(id_str)
        except Exception:
            return False
        res = self.col.update_one({"_id": _id}, {"$set": update_fields})
        return res.modified_count > 0

    def delete_motorista(self, id_str: str) -> bool:
        try:
            _id = ObjectId(id_str)
        except Exception:
            return False
        res = self.col.delete_one({"_id": _id})
        return res.deleted_count > 0

    def add_corrida(self, id_str: str, corrida: Corrida) -> bool:
        try:
            _id = ObjectId(id_str)
        except Exception:
            return False
        res = self.col.update_one({"_id": _id}, {"$push": {"corridas": corrida.to_dict()}})
        return res.modified_count > 0

    def calcular_nota_media(self, id_str: str):
        motorista = self.get_motorista(id_str)
        if not motorista:
            return None
        corridas = motorista.get("corridas", [])
        if not corridas:
            return None
        notas = [c.get("nota", 0) for c in corridas]
        media = sum(notas) / len(notas) if notas else None
        if media is not None:
            self.update_motorista(id_str, {"nota": int(round(media))})
        return media
