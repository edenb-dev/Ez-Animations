
class Waiter():

    def __init__(self, Wait):

        self.Wait = Wait
        self.Time_Till_Animation_Start = 0

    def Animate(self, Time):

        return True if self.Wait <= Time else False


class Animation():

    def __init__(self, Start_Value, End_Value, Animation_Duration, Function, Time_Till_Animation_Start=0):

        self.Start_Value = Start_Value
        self.End_Value = End_Value

        self.Calculated_Value = None  # The Value After The Time Calculation.

        self.Animation_Duration = Animation_Duration  # The Duration Of The Animation.
        self.Time_Till_Animation_Start = Time_Till_Animation_Start  # The Time Needs To Pass Till The Animation Will Start Executing.

        self.Function = Function  # The Function That Preforms The Animation.

    def Animate(self, Current_Time):
        '''
            This Function Calls The 'self.Function' Method With,
            The Calculated Value Based On The Current Time.

            * Return Values :
                True  = The Animation Function Had Finshed.
                False = The Animation Function Is Yet To Finish. 
        '''

        Current_Time = Current_Time - self.Time_Till_Animation_Start

        if Current_Time < self.Animation_Duration:

            # Calculating The New Value To Parse Based On The Current Time.
            self.Calculated_Value = self.Start_Value + (self.End_Value - self.Start_Value) * Current_Time / self.Animation_Duration
            self.Function(self.Calculated_Value)  # Running The Given Function With The Calculated Value.

            return False
        else:

            self.Calculated_Value = self.End_Value
            self.Function(self.Calculated_Value)  # Running The Given Function With The Calculated Value.

            return True
