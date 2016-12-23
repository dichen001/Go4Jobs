"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read, need, buffer = 0, n, ['']*4
        while need > 0:
            k = read4(buffer)
            self.queue.extend(buffer[:k])
            need = min(len(self.queue), n - read)
            buf[read:read+need] = [self.queue.pop(0) for _ in xrange(need)]
            read += need
        return read



        read, EOF = 0, False
        while read < n and not EOF:
            buffer = ['']*4
            k = read4(buffer)
            self.queue.extend(buffer)
            if k < 4:
                EOF = True
            need = min(len(self.queue), n - read)
            for i in range(need):
                buf[read] = self.queue.pop(0)
                read += 1
        return read
