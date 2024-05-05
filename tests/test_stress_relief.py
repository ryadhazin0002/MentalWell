import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):    # Create stress objects for testing
        self.stress = StressFunction()
        self.stress.stresses = [
            Stress(1, "image1.jpg", "Discription 1"),
            Stress(2, "image2.jpg", "Discription 2"),
            Stress(3, "image3.jpg", "Discription 3"),
            Stress(4, "image4.jpg", "Discription 4"),
            Stress(5, "image4.jpg", "Discription 5")
        ]

    def test_current_stress(self):
        # Test initial current stress
        self.assertEqual(self.stress.current_stress(), self.stress.stresses[0])

    def test_iterating_through_current_stress(self): # Test iterating through all stresses
        current_stress = self.stress.current_stress()
        for expected_stress in self.stress.stresses[1:]:
            current_stress = self.stress.next_stress()
            self.assertEqual(current_stress, expected_stress)
        self.assertEqual(self.stress.next_stress(), None)  # Test reaching the end

    def test_previous_stress(self):
        # Move to the last stress
        self.stress.set_current_stress(len(self.stress.stresses) - 1)
        self.assertEqual(self.stress.previous_stress(), self.stress.stresses[-2])

if __name__ == '__main__':
    unittest.main()
