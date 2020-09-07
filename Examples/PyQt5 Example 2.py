

import sys
sys.path.append("..")

from Animator import Animation
from Animation_Manager import Animation_Manager

# ---- PyQt5 - GUI ---- #

from PyQt5.QtWidgets import QApplication, QDesktopWidget  # Must Elements.
from PyQt5.QtWidgets import QWidget, QPushButton  # Elements.


class Window(QWidget):

    # --------------------- Initializing ---------------------- #

    def __init__(self):

        super().__init__()

        # Getting The User's Screen Resolution.
        ScreenGeometry = QDesktopWidget().screenGeometry()

        self.Title = "EZ-Animation Example 2 ( PyQt5 )"

        self.Width = 640
        self.Height = 360

        self.Left = (ScreenGeometry.width() - self.Width) / 2
        self.Top = (ScreenGeometry.height() - self.Height) / 2

        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.Title)
        self.setGeometry(self.Left, self.Top, self.Width, self.Height)

        self.show()

        self.Create_Buttons()  # Loading The Buttons.

    def Create_Buttons(self):

        for Button_Number in range(5):  # Creating 5 Buttons.

            Button = QPushButton("Animate Us", self)  # Creating The Button.
            Button.move(50, 50 + 50 * Button_Number)  # Moving The Button.
            Button.clicked.connect(run_animation)     # Linking The On-Click Function.

            Button.show()   # Showing The Button.

            Button_Group.append(Button)  # Adding The Buttons.

        Group_Animations()  # Adding The Buttons To An Animation Group.


def Load_Animation():

    Animation_Name = 'Movment_Side_To_Side'

    Animation_Sequence = lambda Object: [
        Animation(Start_Value=50,
                  End_Value=500,
                  Animation_Duration=1 + Object.y()/250,
                  Function=lambda New_X_Cords: Object.move(New_X_Cords, Object.y())),
        Animation(Start_Value=500,
                  End_Value=50,
                  Animation_Duration=1 + Object.y()/250,
                  Function=lambda New_X_Cords: Object.move(New_X_Cords, Object.y()),
                  Time_Till_Animation_Start=1 + Object.y()/250)
    ]

    # Adding Animation Sequences.
    Animation_M.Add_Animation_Sequence(Animation_Name, Animation_Sequence)


def Update_Screen():

    # The PyQt5 Some Times Ghosts.
    # This Function Will Prevent That From Happining, By Forcing Updat To The Screen Every 6 Frames.

    global Counter
 
    if Counter % (Animation_M.FPS/15):

        global Main_Window

        Main_Window.update()

    Counter += 1


def Group_Animations():

    # This Function Adds All The Buttons To The Same Animation Group.

    for Button in Button_Group:
        Animation_M.Add_Animation_Queue('Movment_Side_To_Side', Button, On_Finish=on_AnimationFinished, Group_Identifier='Your Group Name')


def run_animation():

    Animation_M.Start_Group_Animation('Your Group Name')

    Group_Animations()  # Adding The Buttons To An Animation Group.


def on_AnimationFinished(Object):
    print("Finished Animating !~!")


if __name__ == "__main__":

    Animation_M = Animation_Manager(FPS=30, Must_Function_Every_Frame=Update_Screen)
    Button_Group = []
    Counter = 0

    Load_Animation()

    # Setting The App.

    App = QApplication(sys.argv)    # Initializing The App.
    Main_Window = Window()          # Loading The Window. ( GUI )
    sys.exit(App.exec())            # Closing The App.
