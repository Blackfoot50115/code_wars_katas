"""
    function cube_checker(volume, side):
        if volume or side <= 0:
            return False
            
            Try:
                if side cubed == volume:
                    return True
                else
                    return False
            Except:
                    return False        
"""
import unittest
from math import pow


def cube_checker(volume, side):
    side_cubed = pow(side, 3)

    if volume <= 0 or side <= 0:
        return False
    else:
        try:
            if side_cubed == volume:
                return True
            else:
                return False
        except:
            return False


class TestCubeChecker(unittest.TestCase):

    def test_cube_checker(self):
        self.assertTrue(cube_checker(8, 2)); pdb.set_trace()


if __name__ == '__main__':
    unittest.main()
