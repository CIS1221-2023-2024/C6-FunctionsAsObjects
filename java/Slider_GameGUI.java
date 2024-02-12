package SliderPuzzle;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JButton;
import javax.swing.JPanel;

public class Slider_GameGUI extends Container {
    private final PuzzleGraphicsPanel puzzleGraphics;
    private final Slider_Game_Model puzzleModel = new Slider_Game_Model();

    // Constructing the GUI
    public Slider_GameGUI() {
        JButton newGameButton = new JButton("New Game");
        newGameButton.addActionListener(new NewGameAction());
        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new FlowLayout());
        controlPanel.add(newGameButton);

        puzzleGraphics = new PuzzleGraphicsPanel();
        this.setLayout(new BorderLayout());
        this.add(controlPanel, BorderLayout.NORTH);
        this.add(puzzleGraphics, BorderLayout.CENTER);
    }

    private class PuzzleGraphicsPanel extends JPanel implements MouseListener {
        private static final int ROWS = 3;
        private static final int COLS = 3;
        private static final int CELL_SIZE = 80; // 80 = pixel size
        private final Font _biggerFont;

        public PuzzleGraphicsPanel() {
            _biggerFont = new Font("SansSerif", Font.BOLD, CELL_SIZE / 2);
            this.setPreferredSize(new Dimension(CELL_SIZE * COLS, CELL_SIZE * ROWS));
            this.setBackground(Color.BLUE);  //choosing background colour
            this.addMouseListener(this);
        }

        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            for (int r = 0; r < ROWS; r++) {
                for (int c = 0; c < COLS; c++) {
                    int x = c * CELL_SIZE;
                    int y = r * CELL_SIZE;
                    String text = puzzleModel.getFace(r, c);
                    if (text != null) {
                        g.setColor(Color.gray);
                        g.fillRect(x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4);
                        g.setColor(Color.black);
                        g.setFont(_biggerFont);
                        g.drawString(text, x + 20, y + (3 * CELL_SIZE) / 4);
                    }
                }
            }
        }

        @Override
        public void mousePressed(MouseEvent e) {
            int col = e.getX() / CELL_SIZE;
            int row = e.getY() / CELL_SIZE;
            if (!puzzleModel._moveTile(row, col)) {
                Toolkit.getDefaultToolkit().beep();
            }
            this.repaint();
        }

        // These methods are required by MouseListener interface but aren't being used
        @Override
        public void mouseClicked(MouseEvent e) { }

        @Override
        public void mouseReleased(MouseEvent e) { }

        @Override
        public void mouseEntered(MouseEvent e) { }

        @Override
        public void mouseExited(MouseEvent e) { }
    }

    private class NewGameAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            puzzleModel.reset();
            puzzleGraphics.repaint();
        }
    }
}


