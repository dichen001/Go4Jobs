/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
*/

public class Solution {
    public boolean isValid(String s) {
        if (s==null || s.length()==0) return true;
        Stack<Character> stack = new Stack<>();
        char[] input = s.toCharArray();
        Map<Character, Character> couple = new HashMap<>();
        couple.put('(', ')');
        couple.put('[', ']');
        couple.put('{', '}');
        for (int i=0; i<input.length; i++){
            if (stack.isEmpty()){
                stack.push(input[i]);
            } else if (couple.containsKey(stack.peek()) && couple.get(stack.peek()) == input[i]){
                stack.pop();
            } else {
                stack.push(input[i]);
            }
        }
        return stack.isEmpty();
    }
}


/*
// Solution in Discussion: faster by using switch directly

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            switch(c) {
                case '(':
                case '{':
                case '[':
                    stack.push(c);
                    break;
                case ']':
                    if (stack.isEmpty() || stack.pop() != '[') return false;
                    break;
                case '}':
                    if (stack.isEmpty() || stack.pop() != '{') return false;
                    break;
                case ')':
                    if (stack.isEmpty() || stack.pop() !='(') return false;
                    break;
            }
        }
        if (stack.isEmpty()) {
            return true;
        }
        return false;
    }
}
*/