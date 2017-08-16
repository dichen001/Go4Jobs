"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def win(pos):
            for i in range(len(pos)-1):
                if mem.get(pos):
                    return mem[pos]
                if pos[i] + 1 == pos[i+1]:
                    tmp = pos[0:i] + pos[i+2:]
                    next = win(tmp)
                    if not next:
                        mem[pos] = True
                        return True
                    else:
                        mem[pos] = False
            return False


        n = len(s)
        mem = {}
        pos = (i for i in range(n) if s[i] == '+')
        return win(pos)


s = Solution()
s.canWin("++++")



