'''Testing for processing.py'''

import unittest

class TestEvent(unittest.TestCase):
    '''For testing the Event class'''

    def test_import(self):
        """ Test that the Processing module can be imported. """
        import Processing
    
    def test_response_time(self):
        '''tests response time'''
        from Processing.processing import Event
        event = Event()
        self.assertIsNotNone(event.response_time().seconds)

if __name__ == '__main__':
    unittest.main()
