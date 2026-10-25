"""Run separately from the repository CI; intentionally failing until solved."""
import unittest
import numpy as np
from starter import vector_dot, matrix_multiply, describe_array

class Tests(unittest.TestCase):
    def test_vector_dot(self):
        self.assertEqual(vector_dot([1, 2, 3], [4, 5, 6]), 32)
        self.assertEqual(vector_dot([], []), 0)
    def test_vector_rejects_bad_shape(self):
        with self.assertRaises(ValueError):
            vector_dot([1,2],[3])
    def test_matmul(self):
        self.assertEqual(matrix_multiply([[1, 2],[3, 4]], [[5, 6],[7, 8]]), [[19, 22],[43, 50]])
        self.assertEqual(matrix_multiply([[1,2,3]], [[1],[2],[3]]), [[14]])
    def test_matmul_rejects_bad_shape(self):
        with self.assertRaises(ValueError):
            matrix_multiply([[1,2]], [[1,2]])
        with self.assertRaises(ValueError):
            matrix_multiply([[1,2],[3]],[[1],[2]])
    def test_describe_array(self):
        self.assertEqual(describe_array(np.array([[1.,2.],[3.,4.]])), ((2,2),2))
        self.assertEqual(describe_array(np.array([1,2,3])), ((3,),1))

if __name__ == '__main__':
    unittest.main()
