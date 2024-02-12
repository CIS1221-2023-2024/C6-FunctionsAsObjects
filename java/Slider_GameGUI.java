package SliderPuzzle;

import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseAdapter;
import javax.swing.*;

public class Slider_GameGUI extends Container {
    private final PuzzleGraphicsPanel puzzleGraphics;
    private final Slider_Game_Model puzzleModel = new Slider_Game_Model();

    // Constructing the GUI
    public Slider_GameGUI() {
        // Initialize puzzleGraphics before using it
        puzzleGraphics = new PuzzleGraphicsPanel();

        JButton newGameButton = new JButton(" Start ");
        newGameButton.addActionListener(e -> {
            puzzleModel.reset();
            puzzleGraphics.repaint();
        });

        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new FlowLayout());
        controlPanel.add(newGameButton);

        JPanel gridPanel = new JPanel(new BorderLayout());
        gridPanel.add(puzzleGraphics, BorderLayout.CENTER);

        this.setLayout(new BorderLayout());
        this.add(controlPanel, BorderLayout.NORTH);  // Here we change the coordinates of the new game button
        this.add(gridPanel, BorderLayout.CENTER);

    }

    public class PuzzleGraphicsPanel extends JPanel {
        private static final int ROWS = 4;
        private static final int COLS = 4;
        private static final int CELL_SIZE = 100; // Pixels
        private final Font _biggerFont;

        public PuzzleGraphicsPanel() {
            _biggerFont = new Font("SansSerif", Font.BOLD, CELL_SIZE / 2);
            this.setPreferredSize(new Dimension(CELL_SIZE * COLS, CELL_SIZE * ROWS));
            this.setBackground(Color.BLACK); //choosing background colour
            this.addMouseListener(new MouseAdapter() {

                public void mousePressed(MouseEvent e) {
                    int col = e.getX() / CELL_SIZE;
                    int row = e.getY() / CELL_SIZE;
                    if (!puzzleModel._moveTile(row, col)) {
                        Toolkit.getDefaultToolkit().beep();
                    }
                    repaint();
                    if (puzzleModel.isPuzzleCompleted()) {

                    }
                }
            });
        }


        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);

            int startX = (this.getWidth() - CELL_SIZE * COLS) / 2;
            int startY = (this.getHeight() - CELL_SIZE * ROWS) / 2;

            // Draw the background for the grid
            g.setColor(Color.BLACK);
            g.fillRect(startX, startY, CELL_SIZE * COLS, CELL_SIZE * ROWS);

            for (int r = 0; r < ROWS; r++) {
                for (int c = 0; c < COLS; c++) {
                    int x = c * CELL_SIZE;
                    int y = r * CELL_SIZE;
                    String text = puzzleModel.getFace(r, c);
                    if (text != null) {
                        g.setColor(Color.white);
                        g.fillRect(x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4);
                        g.setColor(Color.black);
                        g.setFont(_biggerFont);
                        g.drawString(text, x + 20, y + (3 * CELL_SIZE) / 4);
                    }
                }
            }
        }

    }
}
