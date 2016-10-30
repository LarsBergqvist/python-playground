import unittest
from typeCollection import typeCollection, type

class typeCollectionTests(unittest.TestCase):

    def test_getTypeFromId_MatchingObjectExists(self):
        typeList = [type(1),type(2),type(4)]
        coll=typeCollection(typeList)
        self.assertIsNotNone(coll.getTypeFromId(1))
        self.assertIsNotNone(coll.getTypeFromId(2))

    def test_getTypeFromId_MatchingObjectDoesNotExists(self):
        typeList = [type(1),type(2),type(4)]
        coll=typeCollection(typeList)
        self.assertIsNone(coll.getTypeFromId(3))

    def test_getTypeFromId_EmptyCollection(self):
        typeList = []
        coll=typeCollection(typeList)
        self.assertIsNone(coll.getTypeFromId(3))

    def test_getTypeFromId_NoneList(self):
        coll=typeCollection(None)
        self.assertIsNone(coll.getTypeFromId(3))

if __name__ == "__main__": 
    unittest.main()