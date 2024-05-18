import unittest
from unittest.mock import MagicMock, patch
from src.resources import ResourcesFunction


# Mocking the DatabaseManager , #
class MockDatabaseManager:            
    def execute_query(self, query):
        # Mock the query result here
        return [(1, 'image_path1', 'description1', 'video_link1'),    
                (2, 'image_path2', 'description2', 'video_link2')]

class TestResourcesFunction(unittest.TestCase):

    @patch('your_module_name.DatabaseManager', MockDatabaseManager)
    def setUp(self):
        self.resources_func = ResourcesFunction()

    def test_get_all(self):
        resources = self.resources_func.get_all()
        self.assertIsInstance(resources, list)
        self.assertTrue(all(isinstance(res, Resources) for res in resources))

    def test_next_resource(self):
        self.resources_func.set_current_resources(0)
        current_index = self.resources_func.current_resource_index
        next_res = self.resources_func.next_resource()
        self.assertEqual(self.resources_func.current_resource_index, current_index + 1)
        self.assertIsNotNone(next_res)

    def test_previous_resource(self):
        self.resources_func.set_current_resources(1)
        current_index = self.resources_func.current_resource_index
        prev_res = self.resources_func.previous_resource()
        self.assertEqual(self.resources_func.current_resource_index, current_index - 1)
        self.assertIsNotNone(prev_res)

    def test_current_resource(self):
        self.resources_func.set_current_resources(0)
        current_res = self.resources_func.current_resource()
        self.assertEqual(current_res.id, 1)
        self.assertEqual(current_res.image_path, 'image_path1')
        self.assertEqual(current_res.description, 'description1')
        self.assertEqual(current_res.video_link, 'video_link1')


if __name__ == '__main__':
    unittest.main()
