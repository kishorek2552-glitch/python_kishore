class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Process each character from right to left
        for char in reversed(s):
            curr_value = roman_map[char]
            if curr_value < prev_value:
                # Subtract if current numeral is less than the previous
                total -= curr_value
            else:
                # Otherwise, add
                total += curr_value
            prev_value = curr_value

        return total

        