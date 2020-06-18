class CheckVersions:
    # parse version strings into lists
    def __init__(self, str1, str2):
        self.list1 = str1.split('.')
        self.list2 = str2.split('.')
            
    
    def check(self):
        # check if the inputs are valid version numbers
        if(not all(num.isnumeric() for num in self.list1) 
            or not all(num.isnumeric() for num in self.list2)):
            return "Invalid input(s): versions not numbers"

        i = 0
        s = '.'
        # iterate through each list, and compare numbers from first to last
        for num1 in self.list1:
            num2 = self.list2[i]
            
            # compare each digit
            if(self.list1[i] < self.list2[i]):
                return s.join(self.list1) + " is greater than" + s.join(self.list2)
            elif(self.list1[i] > self.list2[i]):
                return s.join(self.list1) + " is greater than " + s.join(self.list2)
            
            i += 1
            
            # version 1 is longer than version 2, but version 2 is contained in version 1
            # inputs are invalid
            # eg: 1.2.2 and 1.2
            if(i > len(self.list2) - 1):
                return "Invalid input(s)"
        
        # version 1 is shorter than version 2, but version 1 is contained in version 2
        # inputs are invalid
        # eg: 1.2 and 1.2.2
        if(len(self.list1) != len(self.list2)):
            return "Invalid input(s)"
        
        # if two lists have the same length and every digit is the same, two versions are the same
        return "Versions are the same"
	