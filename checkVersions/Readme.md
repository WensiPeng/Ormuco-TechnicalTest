Question B

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

In real life, version strings need to follow the following rules:
(1) Version strings should only have numbers. eg: 2.2.a is not acceptable
(2) Version strings can have one or more number of digits. eg: 2, 1.1 and 1.2.3 are all valid versions
(3) Version strings that have different number of digits are comparible. eg: 2.2 is greater than 2.1.2
(4) Version strings that have different number of digits are not comparible if one is contained in another. eg: 2.2 and 2.2.4 are not comparible

Thus, the function should show errors if the above situations happen.

We can first convert strings to lists, and then check if they are all intergers.

If yes, then we can first convert strings to lists of integers, and then compare integers in the 1st and the 2nd version. We start from the first digits of two versions. if two integers are different, we can make the conclusion that one version is greater than the other. If not, we move on to the next digit, until we reach the end of one list.

If the end is reached in only one of the two lists, it means that situation (4) must have happened, so we can show an error message.

If the end is reached in both lists, it means that two versions are exactly the same.

To compare two version string: python main.py
To run the test: python test.pu 