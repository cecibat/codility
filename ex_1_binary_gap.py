"""
A binary gap within a positive integer N is any maximal sequence of 
consecutive zeros that is surrounded by ones at both ends in the binary 
representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap 
of length 2. 
The number 529 has binary representation 1000010001 and contains two binary 
gaps: one of length 4 and one of length 3. 
The number 20 has binary representation 10100 and contains one binary 
gap of length 1. The number 15 has binary representation 1111 and has no 
binary gaps. 
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary 
representation 10000010001 and so its longest binary gap is of length 5. 
Given N = 32 the function should return 0, because N has binary representation 
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

"""
import unittest
MAX_INT = 2147483647

def binary_gap(N):
  
  """
  Check the correctness of the input
  """
  if not isinstance(N, int):
    raise TypeError("The value must be an integer.")
  if N > MAX_INT:
    raise ValueError("The value must be lower or equal than 2,147,483,647.")
  if N < 1:
    raise ValueError("The value must be greater or equal than 1.")
  
  # Convert N to binary and then to string 
  bin_n = str(bin(N)[2:])
  
  # Initialize result and counter, and find the first occurrence of the 0 bit.
  result = 0
  first_zero = bin_n.find('0')
  count = 0
  
  # Go through all the bits and check update the counter at any 0 
  # occurrence, and when the bit flip the result is updated based on the
  # counter value. This ensures that 10000 does not return 4 (because the result
  # is updated only when the bip flips to 1.)
  for bit in bin_n[first_zero:]:
    if bit == '0':
      count += 1
    else:
      result = max(result, count)
      count = 0

  return result

"""
Test cases from codility.com
"""
class TestBinaryGap(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(5, binary_gap(1041))

    def test_example2(self):
        self.assertEqual(0, binary_gap(15))
    
    def test_example3(self):
        self.assertEqual(0, binary_gap(15))
    
    def test_extremes(self):
        self.assertEqual(0, binary_gap(1))
        self.assertEqual(1, binary_gap(5))
        self.assertEqual(0, binary_gap(MAX_INT))

    def test_trailing_zeros(self):
        self.assertEqual(binary_gap(6), 0)
        self.assertEqual(binary_gap(328), 2)

    def test_simple1(self):
        self.assertEqual(binary_gap(9), 2)
        self.assertEqual(binary_gap(11), 1)

    def test_simple2(self):
        self.assertEqual(binary_gap(19), 2)
        self.assertEqual(binary_gap(42), 1)

    def test_simple3(self):
        self.assertEqual(binary_gap(1162), 3)
        self.assertEqual(binary_gap(5), 1)

    def test_medium1(self):
        self.assertEqual(binary_gap(51712), 2)
        self.assertEqual(binary_gap(20), 1)

    def test_medium2(self):
        self.assertEqual(binary_gap(561892), 3)
        self.assertEqual(binary_gap(9), 2)

    def test_medium3(self):
        self.assertEqual(binary_gap(66561), 9)

    def test_large1(self):
        self.assertEqual(binary_gap(6291457), 20)

    def test_large2(self):
        self.assertEqual(binary_gap(74901729), 4)

    def test_large3(self):
        self.assertEqual(binary_gap(805306369), 27)

    def test_large4(self):
        self.assertEqual(binary_gap(1376796946), 5)

    def test_large5(self):
        self.assertEqual(binary_gap(1073741825), 29)

    def test_large6(self):
        self.assertEqual(binary_gap(1610612737), 28)

    def test_input_correctness(self):
        self.assertRaises(TypeError, binary_gap, 1.0)
        self.assertRaises(ValueError, binary_gap, 0)
        self.assertRaises(ValueError, binary_gap, 2147483648)

if __name__ == '__main__':
    binary_gap(894)