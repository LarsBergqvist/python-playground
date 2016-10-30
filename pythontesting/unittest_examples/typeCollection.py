class type:
    id=0
    def __init__(self,id):
        self.id = id

class typeCollection:
    __types = []
    def __init__(self,typeList):
        self.__types = typeList

    def getTypeFromId(self,typeID):
        if self.__types is None:
            return None

        type = next((i for i in self.__types if i.id == typeID), None)
        return type
