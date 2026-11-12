class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        # counts of current window
        counts = {s[0]: 1}
        l, r = 0, 1

        res = 0
        curr_window = 0
        
        while r <= len(s):
            length = r-l
            # count of non-majority characters
            if length - max(counts.values()) <= k: # try expanding
                curr_window = length
                if r < len(s):
                    if s[r] not in counts:
                        counts[s[r]] = 1
                    else:
                        counts[s[r]] += 1
                r += 1
            else: # shrink window
                res = max(res, curr_window)
                counts[s[l]] -= 1
                l += 1

        
        return max(res, curr_window)