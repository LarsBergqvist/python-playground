class Type:
    id=0
    def __init__(self,id):
        self.id = id

class TypeCollection:
    _types = []
    def __init__(self,typeList):
        self._types = typeList

    def get_type_from_id(self,typeID):
        if self._types is None:
            return None

        type = next((i for i in self._types if i.id == typeID), None)
        return type
