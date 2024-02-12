package SliderPuzzle;
import SliderPuzzle.Slider_GameGUI;

import javax.swing.JFrame;

public class Slider_Game {
    public static void main(String[] args) {
        JFrame window = new JFrame("2D-Slider Puzzle Game");
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setContentPane(new Slider_GameGUI());
        window.pack();
        window.setResizable(false);
        window.setVisible(true); // Making sure the window is visible
    }
}


