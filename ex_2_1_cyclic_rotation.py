"""

An array A consisting of N integers is given. Rotation of the array means that 
each element is shifted right by one index, and the last element of the array 
is moved to the first place. For example, the rotation of array 
A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be 
shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the 
array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. 
The performance of your solution will not be the focus of the assessment.
"""
import unittest
def cyclic_rotation(A, K):
  """
  Check the correctness of the input
  """
  N = len(A)
  if not isinstance(K, int):
      raise TypeError("K must be an integer.")
  if K < 0:
    raise ValueError("K must be a positive integer.")
  if K > 100:
    raise ValueError("K must be lower or equal than 100.")
    
  if N > 100:
    raise ValueError("The array must contain at most 100 elements.")
  
  for v in A:
    if not isinstance(v, int):
      raise TypeError("The array must only contain integers.")
    if v < -1000:
      raise ValueError("The minimum allowed value for an element in the array is -1000.")
    if v > 1000:
      raise ValueError("The maximum allowed value for an element in the array is 1000.")
  
  # Early return for corner cases (as many rotations as the array's size, 
  # no rotation, empty array)
  if K == N or K == 0 or N == 0:
    return A
  
  # For each rotation construct a new array, and then assign it to A
  for rot_num in range(K):
    B = A[:-1]
    B.insert(0, A[-1])
    A = B
  return A


"""
Test cases. 
"""
class TestCyclicRotation(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual([], cyclic_rotation([],2))
        
    def test_single_element(self):
        self.assertEqual([2], cyclic_rotation([2],0))
        self.assertEqual([2], cyclic_rotation([2],1))
        self.assertEqual([2], cyclic_rotation([2],5))
        
    def test_double_elements(self):
        self.assertEqual([2,3], cyclic_rotation([2,3],0))
        self.assertEqual([3,2], cyclic_rotation([2,3],1))
        self.assertEqual([2,3], cyclic_rotation([2,3],2))
        self.assertEqual([3,2], cyclic_rotation([2,3],7))
        
    def test_small_vector(self):
        self.assertEqual([3, 8, 9, 7, 6], cyclic_rotation([3, 8, 9, 7, 6],0))
        self.assertEqual([3, 8, 9, 7, 6], cyclic_rotation([3, 8, 9, 7, 6],5))
        self.assertEqual([9, 7, 6, 3, 8], cyclic_rotation([3, 8, 9, 7, 6],3))
    
    def test_large_vector(self):
        expected_value = list(range(98))
        expected_value.insert(0,99)
        expected_value.insert(0,98)
        self.assertEqual(list(range(100)), cyclic_rotation(list(range(100)), 100))
        self.assertEqual(list(range(100)), cyclic_rotation(list(range(100)), 0))
        self.assertEqual(expected_value, cyclic_rotation(list(range(100)), 2))
    
    def test_input_correctness_K(self):
      self.assertRaises(TypeError, cyclic_rotation, [1,2,3,4], 1.0)
      self.assertRaises(ValueError, cyclic_rotation, [1,2,3,4], -1)
      self.assertRaises(ValueError, cyclic_rotation, [1,2,3,4], 101)
      
    def test_input_correctness_A(self):
      self.assertRaises(TypeError, cyclic_rotation, [1.0,2,3,4], 1)
      self.assertRaises(ValueError, cyclic_rotation, [1001,2,3,4], 1)
      self.assertRaises(ValueError, cyclic_rotation, [-1001,2,3,4], 1)
      self.assertRaises(ValueError, cyclic_rotation, list(range(101)), 1)
      
if __name__ == '__main__':
   unittest.main()