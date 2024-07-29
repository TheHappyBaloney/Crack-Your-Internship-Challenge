# 12. Integer to Roman

class Solution:
    def convert_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0

        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def intToRoman(self, num: int) -> str:
        parts = []

        # Extract thousands
        while num >= 1000:
            parts.append(1000)
            num -= 1000

        # Extract hundreds
        if num >= 100:
            hundreds = (num // 100) * 100
            parts.append(hundreds)
            num -= hundreds

        # Extract tens
        if num >= 10:
            tens = (num // 10) * 10
            parts.append(tens)
            num -= tens

        # Extract units
        if num > 0:
            parts.append(num)

        # Convert each part to Roman numerals
        roman_parts = [self.convert_to_roman(part) for part in parts]

        return "".join(roman_parts)
