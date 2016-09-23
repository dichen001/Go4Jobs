/*
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
*/

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        /*
        Assign each element by an position index, then check its uniqueness in a set.
        */
        Set<String> set = new HashSet<String>();
        int size = board.length;
        for (int i=0; i<size; i++){
            for (int j=0; j<size; j++){
                char cell = board[i][j];
                if (cell != '.'){
                    if (!set.add(i+" row "+cell) || !set.add(j+" col "+cell) || !set.add(i/3+" "+j/3+" block "+cell))
                        return false;
                }
            }
        }
        return true;
    }
}