import collections
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        trie = collections.defaultdict(dict)
        for i, s in enumerate(sentences):
            node = trie
            for c in s:
                if c not in node:
                    node[c] = collections.defaultdict(dict)
                node = node[c]
            node['end'] = (times[i], s)
        self.cur = trie

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        ret = []
        if c not in self.cur or c == '#':
            return []
        self.cur = self.cur[c]
        queue = collections.deque([self.cur])
        while queue:
            node = queue.popleft()
            if "end" in node:
                ret.append(node["end"])
            for k, v in node.iteritems():
                if k != "end":
                    queue.append(v)
        return [t[1] for t in sorted(ret, reverse=True)[:3]]






# Your AutocompleteSystem object will be instantiated and called as such:
sentences = ["i love you","island","iroman","i love leetcode"]
times = [5,3,2,2]
obj = AutocompleteSystem(sentences, times)
input, output = "i a#", []
for c in input:
    output.append(obj.input(c))
    print c, output[-1]