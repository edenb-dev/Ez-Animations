
import sys
sys.path.append("..")

from Animation_Manager import Animation_Manager
from Animator import Animation

# ---- PyQt5 - GUI ---- #

from PyQt5.QtWidgets import QWidget, QPushButton  # Elements.
from PyQt5.QtWidgets import QApplication, QDesktopWidget  # Must Elements.


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

        self.Create_Button()  # Loading The Buttons.

    def Create_Button(self):

        Button = QPushButton("Animate Us", self)  # Creating The Button.
        Button.move(50, 50)  # Moving The Button.
        Button.clicked.connect(self.run_animation)     # Linking The On-Click Function.

        Button.show()   # Showing The Button.

    def run_animation(self):

        Object = self.sender()

        Animation_M.Start_Animation("Movment_Along_Border", Object, on_AnimationFinished)


def Load_Animation():

    Animation_Name = 'Movment_Along_Border'

    def Animation_Sequence(Object): return [
        Animation(Start_Value=50,
                  End_Value=500,
                  Animation_Duration=1,
                  Function=lambda New_X_Cords: Object.move(New_X_Cords, Object.y())),
        Animation(Start_Value=50,
                  End_Value=310,
                  Animation_Duration=1,
                  Function=lambda New_Y_Cords: Object.move(Object.x(), New_Y_Cords),
                  Time_Till_Animation_Start=1),
        Animation(Start_Value=500,
                  End_Value=50,
                  Animation_Duration=1,
                  Function=lambda New_X_Cords: Object.move(New_X_Cords, Object.y()),
                  Time_Till_Animation_Start=2),
        Animation(Start_Value=310,
                  End_Value=50,
                  Animation_Duration=1,
                  Function=lambda New_Y_Cords: Object.move(Object.x(), New_Y_Cords),
                  Time_Till_Animation_Start=3)
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


def on_AnimationFinished(Object):
    print("Finished Animating !~!")


if __name__ == "__main__":

    Animation_M = Animation_Manager(FPS=240, Must_Function_Every_Frame=Update_Screen)
    Counter = 0

    Load_Animation()

    # Setting The App.

    App = QApplication(sys.argv)    # Initializing The App.
    Main_Window = Window()          # Loading The Window. ( GUI )
    sys.exit(App.exec())            # Closing The App.
