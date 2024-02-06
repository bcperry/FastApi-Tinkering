'''A sample data processing module'''

from datetime import datetime

class Event: 
    """
    A class to represent a test event.
    ...

    Attributes
    ----------
    startTime : dateTime
        Time the event began
    endTime : dateTime
        Time the event ended

    Methods
    -------
    event_time():
        Calculate the response time for the event.

    """
    def __init__(self, startTime=datetime.now(), endTime=datetime.now()):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            startTime : dateTime
                defaults to the current time
            endTime : dateTime
                defaults to the current time
        """
        self.startTime = startTime
        self.endTime = endTime

    def event_duration(self):
        """
        calculates the time elapsed from event start

        Parameters
        ----------
        None

        Returns
        -------
        startTime : dateTime
        Event time in Seconds
        """
        return self.endTime - self.startTime





if __name__ == '__main__':
    pass