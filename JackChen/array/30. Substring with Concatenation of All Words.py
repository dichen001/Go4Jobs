"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter)
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m, n, l = len(s), len(words), len(words[0])
        need0, missing = {}, n
        for w in words:
            need0[w] = need0.get(w, 0) + 1
        ans = []
        for i in range(m - n*l + 1):
            found, need = 0, need0.copy()
            while found < n:
                w = s[i+found*l:i+(found+1)*l]
                if not need.get(w) or need[w] == 0:
                    break
                need[w] -= 1
                found += 1
            if found == n:
                ans += [i]
        return ans


        result = []
        if not words or len(s) < len(words) * len(words[0]):
            return result
        wl, count, n, word_dict = len(words[0]), len(words), len(s), {}
        for w in words:
            word_dict[w] = word_dict.get(w, 0) + 1
        for i in range(wl):
            start, cnt, tmp_dict = i, 0, {}
            for j in range(i, n-wl+1, wl):
                str = s[j: j+wl]
                if word_dict.get(str):
                    cnt += 1
                    tmp_dict[str] = tmp_dict.get(str,0) + 1
                    while tmp_dict[str] > word_dict[str]:
                        tmp_dict[s[start: start+wl]] -= 1
                        start += wl
                        cnt -= 1
                    if cnt == count:
                        result.append(start)
                        tmp_dict[s[start: start+wl]] -= 1
                        start += wl
                        cnt -= 1
                else:
                    start, cnt, tmp_dict = j+wl, 0, {}
        return result






s = Solution()
print s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
