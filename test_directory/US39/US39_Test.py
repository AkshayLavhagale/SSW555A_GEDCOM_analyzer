"""
User Story 38 - Test File

US39: List upcoming anniversaries
List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days

@Author: Zephyr Zambrano

"""


import unittest, os, io, sys
from ssw555a_ged import GED_Repo, Individual, Family


class Test_US39(unittest.TestCase):
    """ Tests US39. Ensures that upcoming anniversaries are printed to the user. """
    
    def test_US39_upcoming_anniversaries(self):
        """ Tests US39. Ensures that upcoming anniversaries are printed to the user. """
        # upcoming anniversary
        g = GED_Repo([os.path.join(os.getcwd(), "test_directory", "US39", "US39_Upcoming_Anniversaries.ged")])
        self.assertEqual(GED_Repo.US39_print_upcoming_anniversaries(self, [('04/18/1990', 'Husband: Father /Lastname/', 'Wife: Mother /Oldlastname/'), ('04/18/1990', 'Husband: Father /Lastname/', 'Wife: Mother /Oldlastname/'), ('04/18/1990', 'Husband: Father /Lastname/', 'Wife: Mother /Oldlastname/')]), [('04/18/1990', 'Husband: Father /Lastname/', 'Wife: Mother /Oldlastname/'), ('04/18/1990', 'Husband: Father /Lastname/', 'Wife: Mother /Oldlastname/'), ('04/18/1990', 'Husband: Father /Lastname/', 'Wife: Mother /Oldlastname/')])

        # no upcoming anniversary
        g = GED_Repo([os.path.join(os.getcwd(), "test_directory", "US39", "US39_No_Upcoming_Anniversaries.ged")])
        self.assertEqual(GED_Repo.US39_print_upcoming_anniversaries(self, []), "No upcoming anniversaries.")

        # upcoming anniversary, but person is dead so it does not count for this program
        g = GED_Repo([os.path.join(os.getcwd(), "test_directory", "US39", "US39_Dead_Upcoming_Anniversaries.ged")])
        self.assertEqual(GED_Repo.US39_print_upcoming_anniversaries(self, []), "No upcoming anniversaries.")


if __name__ == "__main__":
    unittest.main(exit=False)
