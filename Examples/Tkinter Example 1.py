
import sys
sys.path.append("..")


from Animation_Manager import Animation_Manager
from Animator import Animation

import tkinter as tk


Animation_M = Animation_Manager(FPS=240)


def Load_Animation():

    Animation_Name = 'Movment_Along_Border'

    Animation_Sequence = lambda Object: [
        Animation(Start_Value=50,
                  End_Value=500,
                  Animation_Duration=1,
                  Function=lambda New_X_Cords: Object.place(x=New_X_Cords, y=Object.winfo_y())),
        Animation(Start_Value=50,
                  End_Value=310,
                  Animation_Duration=1,
                  Function=lambda New_Y_Cords: Object.place(x=Object.winfo_x(), y=New_Y_Cords),
                  Time_Till_Animation_Start=1),
        Animation(Start_Value=500,
                  End_Value=50,
                  Animation_Duration=1,
                  Function=lambda New_X_Cords: Object.place(x=New_X_Cords, y=Object.winfo_y()),
                  Time_Till_Animation_Start=2),
        Animation(Start_Value=310,
                  End_Value=50,
                  Animation_Duration=1,
                  Function=lambda New_Y_Cords: Object.place(x=Object.winfo_x(), y=New_Y_Cords),
                  Time_Till_Animation_Start=3)
    ]

    # Adding Animation Sequences.
    Animation_M.Add_Animation_Sequence(Animation_Name, Animation_Sequence)


def run_animation(Object):

    Animation_M.Start_Animation('Movment_Along_Border', Object, On_Finish=on_AnimationFinished)


def on_AnimationFinished(Object):
    print("Finished Animating !~!")


if __name__ == "__main__":

    Load_Animation() # Loading the animation scripts.

    root = tk.Tk()
    root.geometry("640x360")

    My_Button = tk.Button(root, text="Animate Me", command=lambda: run_animation(My_Button))
    My_Button.place(x=50, y=50)

    root.mainloop()
