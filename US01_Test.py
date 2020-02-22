"""
User Story 40 (US40) - Test File
US40: Include input line numbers (when throwing errors)
@Author: Zephyr Zambrano


Classes/Methods throwing errors:
GED_Repo.set_age Individual.us01_check_before_today
GED_Repo.read_ged
GED_REPO.init

"""


import unittest
from ssw555a_ged import GED_Repo, Individual


class Test_GED_Repo(unittest.TestCase):
    """ Tests that errors show """

    def p(self):
        """  d"""
        pass

    def p2(self):
        """  """
        pass

    def test_us01_check_before_today(self):
        """ Tests that us01_check_before_today rejects illegitimate dates by throwing a ValueError. """
        self.assertRaises(ValueError, GED_Repo.us01_check_before_today, self,"40 JAN 1990")
        self.assertRaises(ValueError, GED_Repo.us01_check_before_today, self,"40 DOG 1990")
        self.assertRaises(ValueError, GED_Repo.us01_check_before_today, self,"1 JAN -1")

    def test_set_age(self):
        """ Tests that set_age rejects illegitimate dates by throwing a ValueError. """
        self.assertRaises(ValueError, GED_Repo.us01_check_before_today, self,"40 JAN 1990")
        self.assertRaises(ValueError, GED_Repo.us01_check_before_today, self,"1 DOG 1990")
        self.assertRaises(ValueError, GED_Repo.us01_check_before_today, self,"1 JAN -1")


if __name__ == "__main__":
    unittest.main(exit=False)
