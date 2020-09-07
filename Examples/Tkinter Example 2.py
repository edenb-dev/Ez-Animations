
import sys
sys.path.append("..")

from Animator import Animation
from Animation_Manager import Animation_Manager

import tkinter as tk


Animation_M = Animation_Manager(FPS=240)
Button_Group = []


def Load_Animation():

    Animation_Name = 'Movment_Side_To_Side'

    Animation_Sequence = lambda Object: [
        Animation(Start_Value=50,
                  End_Value=500,
                  Animation_Duration=1 + Object.winfo_y()/250,
                  Function=lambda New_X_Cords: Object.place(x=New_X_Cords, y=Object.winfo_y())),
        Animation(Start_Value=500,
                  End_Value=50,
                  Animation_Duration=1 + Object.winfo_y()/250,
                  Function=lambda New_X_Cords: Object.place(x=New_X_Cords, y=Object.winfo_y()),
                  Time_Till_Animation_Start=1 + Object.winfo_y()/250)
    ]

    # Adding Animation Sequences.
    Animation_M.Add_Animation_Sequence(Animation_Name, Animation_Sequence)


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

    Load_Animation()

    root = tk.Tk()
    root.geometry("640x360")

    for Button_Number in range(5):  # Creating 5 Buttons.

        New_Button = tk.Button(root, text="Animate Us", command=lambda: run_animation())
        New_Button.place(x=50, y=50 + 50 * Button_Number)

        Button_Group.append(New_Button)  # Adding All The Buttons To A List.

    Group_Animations()  # Adding The Buttons To An Animation Group.

    root.mainloop()
