from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def save(self):
        result = super().save()
        return result

    def to_dict(self):
        return {key: value for key, value in self.data.items() if key != "_id"}

    @classmethod
    def list_dicts(cls):
        languages = cls._collection.find({}, {"_id": 0})
        return [language for language in languages]
