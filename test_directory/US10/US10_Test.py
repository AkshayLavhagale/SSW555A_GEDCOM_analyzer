"""
User Story 10 (US10) - Test File
US10: check Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
@Author: Xiaojun zhu
"""

import unittest, os
from ssw555a_ged import GED_Repo

class Test_user_story_10(unittest.TestCase):
    """ Tests that the check_user_story_10 function throws when expected. """

    def test_user_story_10(self):
        """ Tests that check_bday rejects illegitimate Marriage days by throwing a ValueError. """

        # need following cases:
        # birthday before marriage
        self.assertRaises(ValueError, GED_Repo, os.path.join(os.getcwd(), 'test_directory', 'US10', 'US10_Marriage before 14years.ged'))

        # birthday during marriage (normal case)
        # should pass, not sure how to check this
        # self.assertRaises(ValueError, GED_Repo, os.path.join(os.getcwd(), 'test_input_files', 'US08_Birth_After_Marriage.ged'))

        # birthday after divorce (within 9mo)
        # should pass, not sure how to check this
        # self.assertRaises(ValueError, GED_Repo, os.path.join(os.getcwd(), 'test_input_files', 'US08_Birth_After_Divorce_Good.ged'))
        
        # birthday after divorce (after 9mo)
        self.assertRaises(ValueError, GED_Repo, os.path.join(os.getcwd(), 'test_directory', 'US08', 'US08_Birth_After_Divorce_Bad.ged'))

if __name__ == "__main__":
    unittest.main(exit=False)