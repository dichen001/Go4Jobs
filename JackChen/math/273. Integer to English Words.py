"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        t0_19 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',\
                'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',\
                'Eighteen', 'Nineteen']

        t20_90 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def words(num):
            if num < 20:
                return t0_19[num-1:num]
            if num < 100:
                return [t20_90[num/10 -2]] + words(num%10)
            if num < 1000:
                return [t0_19[num/100 -1]] + ['Hundred'] + words(num%100)
            for i, w in enumerate(['Thousand', 'Million', 'Billion'], 1):
                if num < 1000**(i+1):
                    return words(num / 1000**i) + [w] + words(num % 1000**i)
        return ' '.join(words(num)) if num else 'Zero'
