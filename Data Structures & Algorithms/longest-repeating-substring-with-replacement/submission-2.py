class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = r = 0
        sub = 0
        curr_sub = 0
        count[s[l]] = 1
        count[s[r]] = 1

        while r < len(s):
            length = r-l+1
            print(length, count, sub)
            if length - max(count.values()) <= k:
                curr_sub += 1
                r += 1
                if r < len(s) and s[r] not in count:
                    count[s[r]] = 1
                elif r < len(s) and s[r] in count:
                    count[s[r]] += 1
            else:
                sub = max(sub, curr_sub)
                curr_sub -= 1
                count[s[l]] -= 1
                l += 1

        print(count)
        return max(sub, curr_sub)
