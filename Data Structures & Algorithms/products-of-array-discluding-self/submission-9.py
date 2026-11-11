class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        has_zero, has_nonzero = False, False
        res = []

        for num in nums:
            if num == 0:
                if has_zero:
                    return [0 * i for i in range(len(nums))]
                has_zero = True
                continue
            has_nonzero = True
            product *= num
        
        if not has_nonzero:
            return [0 * i for i in range(len(nums))]
        
        for num in nums:
            if num == 0:
                res.append(product)
            elif has_zero:
                res.append(0)
            else:
                res.append(product//num)
        
        return res