from Animator import Waiter


class Animation_Wrapper():

    def __init__(self, Animaiton_List, Object, On_Finish=None):

        self.Animations_In_Progress = Animaiton_List  # List Of Animation That Haven't Finished Animating.
        self.Animations_Processed = []  # List Of Animation That Have Finished Animating.

        self.Animation_Time = 0  # Global Time.

        self.Object = Object
        self.On_Finish = On_Finish

        self.__Verify_Animations__()  # Verifying The Given Animations.

    def Animate(self, Increase_Time_By):
        '''
            This Function Calls The Animate Method Of All The Animations,
            Populating The 'Animations_In_Progress' List.

            When An Animation Had Finished It Is Moved To The 'Animations_Processed' List.

            * Return Values :
                True  = All Animations Had Finshed.
                False = Not All Animation Had Finished. 
        '''

        self.Animation_Time += Increase_Time_By  # Updating The Animation Time.

        # * When Removing An Element, All The Elements Shift Place One Index Back.
        Counter_Elements_Removed = 0  # Counting The Current Number Of Shifted Elements.
        Flagged_Indexes = []  # Holds The Indexes Of Animations That Have Finished To Animate.

        # Animating & Catching The Indexes Of Finshed Animations.
        for Index, Animation in enumerate(self.Animations_In_Progress):  # Going Thru All The Animations.

            if Animation.Time_Till_Animation_Start < self.Animation_Time:  # Checking If The Animation Needs To Be Updated.

                if Animation.Animate(self.Animation_Time):  # Animating The Animation, And Checking If It Had Finsihed.

                    Flagged_Indexes.append(Index - Counter_Elements_Removed)  # Saving The Index Of The Finised Animation.
                    Counter_Elements_Removed += 1  # Updating The Counter.

        # Moving The Elements At The Flagged Index To The 'Animations_Processed' List.
        for Index in Flagged_Indexes:  # Going Thru The Flagged Indexes.

            self.Animations_Processed.append(self.Animations_In_Progress[Index])  # Adding The Animaiton To The 'Animations_Processed' List.
            self.Animations_In_Progress.remove(self.Animations_In_Progress[Index])  # Removing The Animation From The 'Animations_In_Progress' List.

        # Returning True / False Based If All Animaitons Finished Animating.
        return True if not self.Animations_In_Progress else False

    # --------------- Check --------------- #

    def __Verify_Animations__(self):
        '''
            This Function Removes, And Frees Memory Of Any Animations,
            That Aren't Considered As A Valid Animation.
        '''

        # * When Removing An Element, All The Elements Shift Place One Index Back.
        Counter_Elements_Removed = 0  # Counting The Current Number Of Shifted Elements.
        Flagged_Indexes = []  # Indexes Of Elements That Needs To Be Removed. ( After The Shift Calculation )

        Valid_Longest_Animation = 0
        Not_Valid_Longest_Animation = 0

        for Index, Animtion in enumerate(self.Animations_In_Progress):  # Checking For Invalid Animaitons.

            if not self.__Valid_Animation__(Animtion):  # Checking If The Animation Is Invalid.

                Flagged_Indexes.append(Index - Counter_Elements_Removed)  # Saving The Invalid Animation Index.
                Counter_Elements_Removed += 1  # Updating The Counter.

                if Not_Valid_Longest_Animation < Animtion.Time_Till_Animation_Start + Animtion.Animation_Duration:
                    Not_Valid_Longest_Animation = Animtion.Time_Till_Animation_Start + Animtion.Animation_Duration

            else:
                if Valid_Longest_Animation < Animtion.Time_Till_Animation_Start + Animtion.Animation_Duration:
                    Valid_Longest_Animation = Animtion.Time_Till_Animation_Start + Animtion.Animation_Duration

        for Index in Flagged_Indexes:  # Removing The Elements At The Flagged Index.

            self.Animations_In_Progress.remove(self.Animations_In_Progress[Index])

        if Not_Valid_Longest_Animation > Valid_Longest_Animation:
            self.Animations_In_Progress.append(Waiter(Not_Valid_Longest_Animation))

    def __Valid_Animation__(self, Animation):
        '''
            Valid Animaiton Is An Animation That The Value In 'Start' & 'End' Are Not Equal.
        '''

        return True if Animation.Start_Value != Animation.End_Value else False
