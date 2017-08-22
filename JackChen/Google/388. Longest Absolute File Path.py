"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.
Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # concise dict implementation
        max_len, path_len = 0, {0:0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            level = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[level] + len(name))
            else:
                path_len[level + 1] = path_len[level] + len(name) + 1
        return max_len

        # my recent stack implementation
        ans, stack = 0, []
        for s in input.split('\n'):
            sub_path = s.split('\t')
            name = sub_path[-1]
            level = len(sub_path) - 1
            if level >= len(stack):
                stack.append(name)
            else:
                stack[level] = name
            if "." in sub_path[-1]:
                ans = max(ans, len('/'.join(stack[:level+1])))
        return ans

        # my old stack implementation
        result = 0
        inputs = input.split('\n')
        pre, stack = -1, []
        for p in inputs:
            level = p.count('\t')
            name = p[level:]
            if '.' in name:
                cur = '/'.join(stack[:level] + [name])
                result = max(result, len(cur))
                continue
            if level > pre:
                stack.append(name)
            elif level < pre:
                stack = stack[:level] + [name]
            else:
                stack[level] = name
            pre = level
        return result



s = Solution()
# s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
