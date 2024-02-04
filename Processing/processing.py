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
    response_time():
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

    def response_time(self):
        """
        calculates the time elapsed from event start

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None

        Tests
        -----
        >>> e = Event()
        >>> print(e.response_time())
        6
        """
        return datetime.now() - self.startTime

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'t': Event()})