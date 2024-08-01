class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        integer_input = ""
        for digit in digits:
            integer_input += str(digit)
            print(integer_input)
        integer_input = int(integer_input)
        return [int(char) for char in str(integer_input + 1)]
        