class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = []

        res = []
        for value, symbol in value_symbols:
            if num == 0:
                break

            count = num // value
            res.append(symbol * count)
            num -= value * count

        return ' '.join(res)
