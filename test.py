import unittest
from check import CheckVersions

class CheckVersionsTest(unittest.TestCase):
    def checkVersion_InputsEmpty_ShowInputEmpty(self):
        versions = CheckVersions('', '1.2')
        self.assertEqual(versions.check(), "Invalid input(s): versions not numbers")	

    def checkVersion_InputsNotNumbers_ShowInvalidInputs(self):
        versions = CheckVersions('2.2.a', '1.2')
        self.assertEqual(versions.check(), "Invalid input(s): versions not numbers")

    def checkVersion_InputsV1LongerInvalid_ShowInvalidInputs(self):
        versions = CheckVersions('2.2.3', '2.2')
        self.assertEqual(versions.check(), "Invalid input(s)")

    def checkVersion_InputsV2LongerInvalid_ShowInvalidInputs(self):
        versions = CheckVersions('2.2.3', '2.2.3.4')
        self.assertEqual(versions.check(), "Invalid input(s)")

    def checkVersion_InputSame_ShowInputSame(self):
    	versions = CheckVersions('2.2.', '2.2')
    	self.assertEqual(versions.check(), "Versions are the same")

    def checkVersion_InputsSameLengthV1Greater_ShowV1Greater(self):
        versions = CheckVersions('2.2.3', '1.3.3')
        self.assertEqual(versions.check(), "2.2.3 is greater than 1.3.3")

    def checkVersion_InputsSameLengthV2Greater_ShowV2Greater(self):
        versions = CheckVersions('1.2.3', '3.3.3')
        self.assertEqual(versions.check(), "3.3.3 is greater than 1.2.3")

    def checkVersion_InputsV1LongerV1Greater_ShowV1Greater(self):
        versions = CheckVersions('3.2.1', '1.3')
        self.assertEqual(versions.check(), "3.2.1 is greater than 1.3")

    def checkVersion_InputsV1LongerV2Greater_ShowV2Greater(self):
        versions = CheckVersions('2.2.1', '2.3')
        self.assertEqual(versions.check(), "2.2.1 is greater than 2.3")
    
    def checkVersion_InputsV2LongerV1Greater_ShowV1Greater(self):
        versions = CheckVersions('1.4', '1.3.3')
        self.assertEqual(versions.check(), "1.4 is greater than 1.3.3")

    def checkVersion_InputsV2LongerV2Greater_ShowV2Greater(self):
        versions = CheckVersions('2.2', '2.3.3')
        self.assertEqual(versions.check(), "2.2 is greater than 2.3.3")


if __name__ == '__main__':
    unittest.main()