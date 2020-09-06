from time import time as Time
from time import sleep as Sleep

from threading import Thread


class Repeated_Timer():

    def __init__(self, Interval, Task, *Args, **KWArgs):

        self.Interval = Interval    # The Amount Of Time Between Function Executions.
        self.Task = Task            # The Function To Be Executed.

        self.Args = Args            # Parsed Arguments.
        self.KWArgs = KWArgs        # Parsed Keyword Arguments.

        self.__Stop_Flag__ = True   # Indicates When To Stop Repeating The Timer. ( Task )

    def Start(self):  # Start's The Repeat Method.

        if self.__Stop_Flag__:  # Making Sure That The Timer Isn't Running.

            self.__Stop_Flag__ = False  # Updating The Stop Indicator.

            Thread(target=self.__Repeat__).start()  # Init And Starting The Thread.

    def Stop(self):  # Stop's The Repeat Method.

        self.__Stop_Flag__ = True  # Updating The Stop Indicator.

    def __Repeat__(self):

        # This Method Executes The Given Task Repeatedly.

            # Explanation :

                # The Method Uses 'Estimated_Sleep_Time' and 'After_Task_Sleep_Time',
                # To Calculate The Needed Sleep Time, In Order To Prevent Task Drifting.

                # Task Drifting :

                    # Is When A Task Takes Longer Then Estimated To Execute, And The
                    # Following Tasks, Executig With An Unwanted Delay.

                # Estimated_Sleep_Time :

                    # Is The Time The User Rquested To Wait, Between Task Executions.

                # After_Task_Sleep_Time :

                    # Is The Time Left To Sleep, After The Task Was Executed.

        # Pre-Calculations :
        Estimated_Sleep_Time = Time() + self.Interval

        while not self.__Stop_Flag__:  # Contunie Executing, If The Stop Flag Is False.

            try:  # Executing The Task.

                self.Task(*self.Args, **self.KWArgs)

            except Exception as Error:

                print(f'An Error Has Occurred While Executing The Task :\n{Error}')

            After_Task_Sleep_Time = max(0, Estimated_Sleep_Time - Time())  # Preventing Task Drifting.

            Sleep(After_Task_Sleep_Time)  # Calculating The New Sleep Time.

            Estimated_Sleep_Time += self.Interval  # Updating The 'Estimated_Sleep_Time'.
