#!/usr/bin/python3
""" this is the unittest of base_model.py

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import os
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """ Unittests for testing BaseModel class. """
    def test_attributes(self):
        """ test for datetime set in create and update"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """ Test output of string to expected """
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)

    def test_save(self):
        """ Test for save """
        model = BaseModel()
        with patch.object(model, 'updated_at') as mock:
            model.save()
            mock.assert_called_once()

    def test_to_dict(self):
        """ Test for dict values """
        model = BaseModel()
        expected_dict = {
                'id': model.id,
                'created_at': model.created_at.isoformat(),
                'updated_at': model.updated_at.isoformat(),
                '__class__': 'BaseModel',
        }
        self.assertDictEqual(model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
