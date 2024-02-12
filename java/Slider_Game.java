package SliderPuzzle;

import javax.swing.JFrame;
import java.awt.Dimension;

public class Slider_Game {
    public static void main(String[] args) {
        JFrame window = new JFrame("2D-Slider Puzzle Game");
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setContentPane(new Slider_GameGUI());
        window.pack();
        window.setResizable(true);

        window.setSize(new Dimension(1000, 800));

        window.setVisible(true);// Make sure the window is visible

    }


