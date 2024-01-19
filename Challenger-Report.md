# Report: Functions As Objects
### Brainstorming Session
Initially, I contacted the team to work on and discuss the project together. After some time, we decided to talk to the professor about what the scope of the project should consist of. After the discussion, the team decided to implement a slider puzzle game. This is a type of puzzle where the objective is to rearrange pieces on a board to achieve a particular sequence from a shuffled one. I agreed with the team that this project would be an appropriate choice since it would allow for the usage of the concepts of the project: **Functions as Objects**, **Lambda Expressions**, and **Object Oriented Programming**.

### Program Design and Concept Integration
I suggested that two identical programs be made, one in Python, and the other in Java. This is since they both have very useful packages to allow for easy coding of such a game. Additionally other packages for the game include:
- **pygame** - provides functionalities to create games, multimedia applications, and simulations in Python
- **tkinter** - Tk GUI toolkit and provides a simple way to create windows, dialogs, buttons, entry fields, and other GUI elements in Python
- **Swing** - widget toolkit for GUI in Java
- **javax.swing** package consists of classes for the Java Swing API such as JButton, JTextField, JLabel, JMenu, etc. 
- **java.awt.event** - package which is commonly used in Java for handling events in GUIs

These languages are also optimal choices for supporting a program centered around **Object Oriented paradigm**, they would allow to make use of code reorganization and reusability. Additionally, the team could compare the functionality that these two languages and the specified packages provide.

The **event handler** could be used to each puzzle piece, causing an event when clicked and moved around. **Lambda expressions** are used to create anonymous functions that capture the current row and column of the clicked puzzle piece. **Objects** can be used to represent each individual puzzle piece, encapsulating their state and behavior, as well as managing the puzzle as a whole including its pieces and the logic for shuffling.

### Technical Configurations

Additionally, the team and I had met up again to configure their Git and IDE features. I helped them install the necessary tools, cloned the repository on their devices, downloaded GitHub Desktop, and showed them how to push and pull into the repository so that they can effectively work on the project together. Afterwards, I suggested a couple [helpful resources](https://github.com/CIS1221-2023-2024/C6-FunctionsAsObjects/discussions/3).

### Current view of the project
The current project on GitHub as of the date of this commit, contains a number grid that allows the user to click and shift the blocks, in order to align them by ascending order, in which case they would 'win' the game. The project also has a functioning shuffle button that changes the position of the numbers on the grid.

### Suggestions and Comments

Unfortunately, time will not allow me to implement changes in the code myself due to a later submission date than expected. Although, I can provide suggestions about the way this  program could be implemented in a better way:
-	Adding a function that detects that the user has won the game with a message or animations.
-	Starting the program with an already shuffled board/ create a start screen/button.
-	Adding a timer to track how much time it takes the user to complete the puzzle.
-	To further improve responsiveness, add sound effects, score functions etc.
-	Ensuring the puzzle shuffle scheme is algorithmically solvable.
-	Adding short sound effects when an event like shuffling a tile occurs.
  
In relation to your project’s programming concepts:

Lambda expressions can be utilized for:
  - short, throw-away functions or to display one time-messages, things like the ‘Game Started!’ or ‘Game Won!’
  - timer updates, generating a random number
 	
Object Oriented Principles:
  - As already done in your project, having multiple classes (grid, button, main) that utilize inheritance and encapsulate their own functionality to make the code more modular and maintainable.
 	
Event Handling:
  - Also already utilized in your project as event handlers are used when the user clicks on a number or button. Event handling loop in main while running:  

```
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_handler.handle_click(pygame.mouse.get_pos())
```

### Conclusion
Overall, I wish time allowed us to further collaborate and build more onto this project. I think the team did a good job in utilizing the OOP and event handling concepts as well as picking what packages to utilize and how to structure the functions into different classes.  
