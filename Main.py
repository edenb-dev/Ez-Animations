
from Animator import Animation
from Animation_Manager import Animation_Manager


class Cube():

    def __init__(self):

        self.x = 0
        self.y = 0
        self.new_x = 5
        self.new_y = 5

    def Move(self, x, y):

        self.x = x
        self.y = y

        print('cords : ', self.x, ':', self.y)


def Main():

    Cube_Object = Cube()

    # --------- #

    Animation_Name = 'Cube_Movment'

    Animation_Sequences = [lambda Object: [
        Animation(Start_Value=Object.x,
                  End_Value=Object.x + Object.new_x,
                  Animation_Duration=5,
                  Function=lambda New_X_Cords: Object.Move(New_X_Cords, Object.y)),
        Animation(Start_Value=Object.y,
                  End_Value=Object.y + Object.new_y,
                  Animation_Duration=5,
                  Function=lambda New_Y_Cords: Object.Move(Object.x, New_Y_Cords))
    ]]

    # --------- #

    Animation_M = Animation_Manager(FPS=20)

    # Adding Animation Sequences.
    Animation_M.Add_Animation_Sequence(Animation_Name, Animation_Sequences[0])

    # Creating Temp Groups For Testing.

    Group_Number = 50
    Objects_Per_Group = 2

    for Group_Idenifier in range(Group_Number):
        for _ in range(Objects_Per_Group):
            Animation_M.Add_Animation_Queue('Cube_Movment', Cube_Object, str(Group_Idenifier))

    # Showing All The Groups.
    # for (Group, Value) in  Animation_M.Animation_Queue.items():
    #     print(Group)

    # Testing All The Possible Start Options.
    # Animation_M.Start_All_Animations()
    # Animation_M.Start_Group_Animation('3','7','1')
    Animation_M.Start_Animation('Cube_Movment', Cube_Object)

    # Showing The Objects That Are Currntly Being Animated.
    # for Animated_Object in Animation_M.Animated_Objects_List:
    #     print(Animated_Object)


if __name__ == "__main__":

    Main()
