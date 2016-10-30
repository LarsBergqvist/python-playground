import unittest
from typecollection import TypeCollection, Type

class TypeCollectionTests(unittest.TestCase):

    def test_get_type_from_id_matching_object_exists(self):
        typeList = [Type(1),Type(2),Type(4)]
        coll=TypeCollection(typeList)
        self.assertIsNotNone(coll.get_type_from_id(1))
        self.assertIsNotNone(coll.get_type_from_id(2))

    def test_get_type_from_id_not_matching_object(self):
        typeList = [Type(1),Type(2),Type(4)]
        coll=TypeCollection(typeList)
        self.assertIsNone(coll.get_type_from_id(3))

    def test_get_type_from_id_empty_collection(self):
        typeList = []
        coll=TypeCollection(typeList)
        self.assertIsNone(coll.get_type_from_id(3))

    def test_get_type_from_id_collection_initiated_with_none_list(self):
        coll=TypeCollection(None)
        self.assertIsNone(coll.get_type_from_id(3))

if __name__ == "__main__": 
    unittest.main()