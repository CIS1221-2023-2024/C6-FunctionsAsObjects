package SliderPuzzle;

import javax.swing.JOptionPane;
public class Slider_Game_Model {
    private static final int ROWS = 4;  // number of rows
    private static final int COLS = 4; // number of coloums
    private Tile[][] contents;
    private Tile emptyTile;

    public Slider_Game_Model() {
        contents = new Tile[ROWS][COLS];
        reset();
    }

    public String getFace(int row, int col) {
        if (contents[row][col] == null) {
            return null;
        }
        return contents[row][col].getFace();
    }

    // Reseting the game
    public void reset() {
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                contents[r][c] = new Tile(r, c, "" + (r * COLS + c + 1));

            }
        }
        emptyTile = contents[ROWS - 1][COLS - 1];
        emptyTile.setFace(null);

        do {
            // Shuffle the tiles
            for (int i = 0; i < ROWS * COLS * 26; i++) {
                int r = (int) (Math.random() * ROWS);
                int c = (int) (Math.random() * COLS);
                _moveTile(r, c);
            }
        }while(!isPuzzleSolvable());
    }
private boolean isPuzzleSolvable(){
    int reverse = Num_Reverse();
    int blankRowFromBottom = ROWS - (emptyTile.row + 1);
    if (ROWS % 2 == 0) { // If the grid is even
        return (blankRowFromBottom % 2 == 0) == (reverse % 2 != 0);
    } else { // If the grid is odd
        return reverse% 2 == 0;
    }
}
    public boolean _moveTile(int r, int c) {
        return checkEmpty(r, c, -1, 0) || checkEmpty(r, c, 1, 0) ||
                checkEmpty(r, c, 0, -1) || checkEmpty(r, c, 0, 1);
    }

    private boolean checkEmpty(int r, int c, int rdelta, int cdelta) {
        int rNeighbor = r + rdelta;
        int cNeighbor = c + cdelta;
        if (isLegalRowCol(rNeighbor, cNeighbor) && contents[rNeighbor][cNeighbor] == emptyTile) {
            exchangeTiles(r, c, rNeighbor, cNeighbor);
            return true;
        }
        return false;
    }

    // switching positions between 2 tiles
    private void exchangeTiles(int r1, int c1, int r2, int c2) {
        Tile temp = contents[r1][c1];
        contents[r1][c1] = contents[r2][c2];
        contents[r2][c2] = temp;
    }

    public boolean isLegalRowCol(int r, int c) {
        return r >= 0 && r < ROWS && c >= 0 && c < COLS;
    }

    private int Num_Reverse(){
        int reverse = 0;
        for (int i = 0; i < ROWS * COLS; i++) {
            int currentRow = i / COLS;
            int currentValue = contents[currentRow][i % COLS] != emptyTile ? Integer.parseInt(contents[currentRow][i % COLS].getFace()) : 0;
            if (currentValue != 0) {
                for (int j = i + 1; j < ROWS * COLS; j++) {
                    int nextRow = j / COLS;
                    int nextValue = contents[nextRow][j % COLS] != emptyTile ? Integer.parseInt(contents[nextRow][j % COLS].getFace()) : 0;
                    if (currentValue > nextValue && nextValue != 0) {
                        reverse++;
                    }
                }
            }
        }
        return reverse;

    }

    // checking if game is over
    public boolean isPuzzleCompleted() {
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                Tile tile = contents[r][c];
                if (!tile.isInFinalPosition(r, c)) {
                    return false;
                }
            }
        }

        JOptionPane.showMessageDialog(null,
                "Congratulations, You Won The Game!\n");
        return true;
    }

    class Tile {
        private int row;
        private int col;
        private String face;

        public Tile(int row, int col, String face) {
            this.row = row;
            this.col = col;
            this.face = face;
        }

        public void setFace(String newFace) {
            face = newFace;
        }

        public String
        getFace() {
            return face;
        }

        public boolean isInFinalPosition(int r, int c) {
            return r == row && c == col;
        }
    }
}
Write to India Vella
