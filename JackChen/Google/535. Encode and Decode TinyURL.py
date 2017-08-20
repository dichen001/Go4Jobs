"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""

from random import randint
class Codec:
    def __init__(self):
        self.a = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mem = {}


    def getRand(self):
        key = []
        for i in range(6):
            key += [self.a[randint(0, 61)]]
        return ''.join(key)


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = self.getRand()
        while key in self.mem:
            key = self.getRand()
        self.mem[key] = longUrl
        return "www.tiny.dd/" + key


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.mem[shortUrl[len("www.tiny.dd/"):]]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
