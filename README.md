# Ez-Animations
Python library, that helps you create animation with ease, to any python GUI framework.

## Intorduction

The Ez-Animations lib, add's the abilty to create animation scripts, link them to objects / groups of objects, and then animate them separately or all at once.<br>
Also the lib provides you with the ability to control the fps of the animation scripts, based on your preferences.


* Animation Scripts (Animation Sequences) - Reusable sequence of animations, that will perform the animation on the selected object.


### Pre-Knowledge Requirements.
Before you do anything with this lib, you need to understand fully the GUI framework that you are working with.<br>
You need to know exactly how to move, scale, rotate, change alpha, etc, inorder to create your own animation scripts, that supports those actions. 



## How to use

**This example will show you how to create a simple animaiton using the library with the tkinter GUI framework.**

1. Download the files, and place it in a known directory.
2. Import the modules 'Animation', 'Animation_Manager' and 'tkinter' to your python project.

```
from Animator import Animation
from Animation_Manager import Animation_Manager

import tkinter as tk # GUI Framework
```

3. Initialize the Animation_Manager object, with the FPS count you would like to use.

```
Animation_M = Animation_Manager(FPS=60)
```

4. Create & Load your animaiton sequence.

The animaiton sequence is an array filled with Animation objects. Each Animation object has several settings.

* Start_Value - The starting value.
* End_Value   - The ending value.
* Animation_Duration - The duration the animation will take.
* Function    - The logic on how to perform the animation.
* Time_Till_Animation_Start - The duration to wait before the animation will start. **( Optional )**

*This simple script will move the object given, along the border of the window, and will complete a full rotation*


<details>
  <summary>Click To Show Code</summary>
  
```
  Animation_Name = 'Movment_Along_Border'

  Animation_Sequence = lambda Object: [
          Animation(Start_Value=50,   # Moving From Left To Right.
                    End_Value=500,
                    Animation_Duration=1,
                    Function=lambda New_X_Cords: Object.place(x=New_X_Cords, y=Object.winfo_y())),
          Animation(Start_Value=50,   # Moving From Top To Bottom.
                    End_Value=310,
                    Animation_Duration=1,
                    Function=lambda New_Y_Cords: Object.place(x=Object.winfo_x(), y=New_Y_Cords),
                    Time_Till_Animation_Start=1),
          Animation(Start_Value=500,  # Moving From Right To Left.
                    End_Value=50,
                    Animation_Duration=1,
                    Function=lambda New_X_Cords: Object.place(x=New_X_Cords, y=Object.winfo_y()),
                    Time_Till_Animation_Start=2),
          Animation(Start_Value=310,  # Moving From Bottom To Top.
                    End_Value=50,
                    Animation_Duration=1,
                    Function=lambda New_Y_Cords: Object.place(x=Object.winfo_x(), y=New_Y_Cords),
                    Time_Till_Animation_Start=3)
  ]

  # Adding/Loading The Animation Sequence.
  Animation_M.Add_Animation_Sequence(Animation_Name, Animation_Sequence)
```
</details>


5. Add a function to start the animation.

Start Animation takes several parameters :

* Animation Name - The name of the animation, that was added to the Animation_Manager
* Object - The object that the animation will be performed on.
* On_Finish - Function that will excute once the animation finishes. **( Optional )**<br>On_Finish also passes to the function the object used in the animation. 

```
def run_Animation(Object):

    Animation_M.Start_Animation('Movment_Along_Border', Object, On_Finish=on_AnimationFinished)
```

Add the following code, only if you added the On_Finish parameter.

```
def on_AnimationFinished(Object):
    print("Finished Animating !~!")
```

6. Finally create the tkinter window with a button, that when clicked excutes the run_Animation function.

```    
    root = tk.Tk()
    root.geometry("640x360")

    My_Button = tk.Button(root, text="Animate Me", command=lambda: run_animation(My_Button))
    My_Button.place(x=50, y=50)

    root.mainloop()
```

### More Examples Could Be Found In [Example]()

## Built With

* [Ez_Timers](https://github.com/edenb-dev/Ez-Timers) - Used to for time management.
