
# EzTimes Lib:
from EzTimes.Ez_Timers import Repeated_Timer


from Animation_Wrapper import Animation_Wrapper


class Animation_Manager():

    def __init__(self, FPS=60):

        self.FPS = 1/FPS                # Times Per Sec The Animator Will Update.
        self.Animation_Sequences = {}   # Animation Scripts. ( Key = Animation_Name , Value = Animation_Sequence)
        self.Animation_Queue = {}       # Groups Of Objects & Their Animation Script, That Can Be Processed \ Animated Together.
        self.Animated_Objects_List = []  # The Objects That Are Currently Being Animated.

        self._Is_Running = False            # Flag That Indicates If The Timer Is Currently Running.
        self._All_Group_Activated = False   # Flag That Indicates If All The Groups Activated At The Same Time.
        self._Finished_Loading = 0          # When At 0 Indicates That All The Objects Have Loaded, To The 'Animated_Object_List'.

        self.Repeated_Timer = Repeated_Timer(self.FPS, self.Upadting_Animation)

    # ----------------------------------------------------- #

    def Add_Animation_Sequence(self, Animation_Name, Animation_Sequence):
        '''
            This Lets The User Add New Animaiton Sequences.
        '''

        self.Animation_Sequences.update({Animation_Name: Animation_Sequence})  # Updating The 'Animation_Sequences'.

    def Add_Animation_Queue(self, Animation_Name, Object, Group_Identifier):
        '''
            This Function Lets The User Group Objects,
            To Be Animated Together.

            When The Function 'Start_Group_Animation' Executed With The Group Identifier.
        '''

        if self.Animation_Queue.get(Group_Identifier) is None:  # Checking If The Group Exists.
            self.Animation_Queue.update({Group_Identifier: []})  # Allocating Memory For The New Group.

        # Adding The Object To The Group.
        Temp_List = self.Animation_Queue.get(Group_Identifier)
        Temp_List.append({'Animation_Name': Animation_Name, 'Object': Object})
        self.Animation_Queue.update({Group_Identifier: Temp_List})

    # ------------- Start Animation Functions ------------- #

    def Start_All_Animations(self):
        '''
            Starts All The Animations, In All The Groups.
        '''

        self._All_Group_Activated = True    # Setting The Flag.

        for (Group_Identifier, Group_Value) in self.Animation_Queue.items():  # Updating The Number Of Objects Needed To Be Loaded From The 'Animation_Queue'.
            self._Finished_Loading += len(Group_Value)

        for (Group_Identifier, Group_Value) in self.Animation_Queue.items():  # Running Thru The Groups.
            self.Start_Group_Animation(Group_Identifier)

    def Start_Group_Animation(self, *Groups_Identifiers):
        '''
            Starts All The Animations In The Specified Groups Identifiers.

            * Groups_Identifiers -> List Of One Or More 'Group_Identifier'.
        '''

        if not self._All_Group_Activated:   # Updating The Number Of Objects Needed To Be Loaded From The 'Animation_Queue'.

            for Group_Identifier in Groups_Identifiers:  # Running Thru All The Groups Identifiers.
                self._Finished_Loading += len(self.Animation_Queue.get(Group_Identifier))

        for Group_Identifier in Groups_Identifiers:  # Running Thru All The Groups Identifiers.
            for Animation_Element in self.Animation_Queue.get(Group_Identifier):  # Running Thru All The Objects In The Group.
                self.Start_Animation(Animation_Element.get('Animation_Name'), Animation_Element.get('Object'))  # Starting The Animation On The Object.

    def Start_Animation(self, Animation_Name, Object):
        '''
            Start The Aninmation Of One Object.
        '''

        self.Animated_Objects_List.append(Animation_Wrapper(self.Animation_Sequences.get(Animation_Name)(Object)))

        if self._Finished_Loading > 1:  # Checking If More Then One Object Need To Loaded.

            self._Finished_Loading -= 1

        else:

            if self._Finished_Loading != 0:  # Checking If Finished Loading All The Objects.

                self._Finished_Loading -= 1

            if not self._Is_Running:  # Checking If The Clock Is Running.

                self.Start_Clock()  # Starting The Clock.

    # -------- Clock & Update Animation Functions --------- #

    def Start_Clock(self):

        self._Is_Running = True

        self.Repeated_Timer.Start()

    def Stop_Clock(self):

        self._Is_Running = False

        self.Repeated_Timer.Stop()

    def Upadting_Animation(self):

        if self.Animated_Objects_List:  # Checking If There Are Animations To Animate.

            # * When Removing An Element, All The Elements Shift Place One Index Back.
            Counter_Elements_Removed = 0  # Counting The Current Number Of Shifted Elements.
            Flagged_Indexes = []  # Holds The Indexes Of Animations That Have Finished To Animate.

            for Index, Animation_Wrap in enumerate(self.Animated_Objects_List):

                if Animation_Wrap.Animate(self.FPS):

                    Flagged_Indexes.append(Index - Counter_Elements_Removed)  # Saving The Index Of The Finised Animation.
                    Counter_Elements_Removed += 1  # Updating The Counter.

            # Removing Elements At The Flagged Index From The 'Animated_Objects_List' List.
            for Index in Flagged_Indexes:  # Going Thru The Flagged Indexes.

                self.Animated_Objects_List.remove(self.Animated_Objects_List[Index])  # Removing The Animation From The 'Animated_Objects_List' List.

            if not self.Animated_Objects_List:  # Checking If All Animations Had Finished.

                self.Stop_Clock()  # Stopping The Clock.

        else:  # No Animations To Animate.

            self.Stop_Clock()  # Stopping The Clock.
