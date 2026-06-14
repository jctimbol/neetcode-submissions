class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f"{n:032b}"
        reverse = ""
        for i in range(0, 32):
            reverse += binary[31-i]
        return int(reverse,2)