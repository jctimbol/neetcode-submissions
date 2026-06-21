class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        in_str = ""
        for digit in digits:
            in_str += str(digit)

        in_num = int(in_str)
        out_num = in_num + 1
        out_str = str(out_num)
        return list(out_str)