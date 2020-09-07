# Ez-Animations
Python library, that helps you create animation with ease, to any python GUI framework.

## Intorduction

The Ez-Animations lib, add's the abilty to create animation scripts, link them to objects / groups of objects, and then animate them separately or all at once.<br>
The Ez-Animations lib, also provides you will the ability to control the fps of the animation scripts, based on your preferences.


* Animation Scripts (Animation Sequences) - Reusable sequence of animations, that will perform the animation on the selected object.


### Pre-Knowledge Requirements.
Before you do anything with this lib, you need to understand fully the GUI framework that you are working with.<br>
You need to know exactly how to move, scale, rotate, change alpha, etc, inorder to create your own animation scripts, that supports those actions. 



## How to use

**This example will show you how to create a simple animaiton using the library with the tkinter GUI framework.**

1. Download the files, and place it in a known directory.
2. Import the modules 'Animation' and 'Animation_Manager' to your python project.

```
from Animator import Animation
from Animation_Manager import Animation_Manager
```
3. Initialize the Animation_Manager object, with the FPS count you would like to use.

*This is done in the global scope.*

```
Animation_M = Animation_Manager(FPS=60)
```
4. Load your animation sequence, into your Animation_Manager object.
4. Create your animaiton sequence.

The animaiton sequence is an array filled with Animation objects.
Each Animation object has several settings.
* Start_Value - The starting value.
* End_Value   - The ending value.
* Animation_Duration - The duration the animation will take.
* Function    - The logic on how to perform the animation.
* Time_Till_Animation_Start - The duration to wait before the animation will start.




