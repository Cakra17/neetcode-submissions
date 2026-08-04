class Solution {
public:
    bool checkRowAndCol(
      vector<vector<char>>&board, 
      const char& c, int row, int col
    ) {
      for (int i = 0; i < board.size(); i++) {
        if (board[row][i] == c && i != col) {
          return false;
        }

        if (board[i][col] == c && i != row) {
          return false;
        }
      }
      return true;
    }

    bool checkSubGrid(
      vector<vector<char>>&board, 
      const char& c, int row, int col
    ) {
      int x = row/3 * 3;
      int y = col/3 * 3;
      for (int i = x; i < x+3; i++) {
        for (int j = y; j < y+3; j++) {
          if (board[i][j] == c && i != row && j != col) {
            return false;
          }
        }
      }
      return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
      for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
          if (board[i][j] != '.') {
            bool rule1 = checkRowAndCol(board, board[i][j], i, j);
            bool rule2 = checkSubGrid(board, board[i][j], i, j);
            if (!rule1 || !rule2) {
              return false;
            }
          }
        }
      }
      return true;
    }
};
