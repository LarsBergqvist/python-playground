#!/usr/bin/env python3

class Type:
    id = 0

    def __init__(self, identifier):
        self.id = identifier


class TypeCollection:
    _types = []

    def __init__(self, typeList):
        self._types = typeList

    def get_type_from_id(self, typeid):
        if self._types is None:
            return None

        mytype = next((i for i in self._types if i.id == typeid), None)
        return mytype
