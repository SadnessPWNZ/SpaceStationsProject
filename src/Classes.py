'''

Project code classes here

'''


class Pass:
    def __init__(self, startAz: float, startAzCompass: str, startTime: str, maxAz: float, maxAzCompass: str,
                 maxTime: str, endAz: float, endAzCompass: str, endTime: str, mag: float, duration: int):
        '''

        :param startAz: Satellite azimuth for the start of this pass (relative to the observer, in degrees)
        :param startAzCompass: Satellite azimuth for the start of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
        :param startTime: Start time
        :param maxAz: Satellite azimuth for the max elevation of this pass (relative to the observer, in degrees)
        :param maxAzCompass: Satellite azimuth for the max elevation of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
        :param maxTime: Time for the max elevation of this pass.
        :param endAz: Satellite azimuth for the end of this pass (relative to the observer, in degrees)
        :param endAzCompass: Satellite azimuth for the end of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
        :param endTime: Time for the end of this pass.
        :param mag: Max visual magnitude of the pass, same scale as star brightness. If magnitude cannot be determined, the value is 100000
        :param duration:  Total visible duration of this pass (in seconds)
        '''
        self.startAz, self.startAzCompass, self.startTime, self.maxAz, self.maxAzCompass, self.maxTime, self.endAz, \
        self.endAzCompass, self.endTime, self.mag, self.duration = startAz, startAzCompass, startTime, maxAz, \
                                                                   maxAzCompass, maxTime, endAz, endAzCompass, endTime, mag, duration

    def __str__(self):
        return f'Start Azimuth:{self.startAz}\n' \
            f'Start Azimuth on Compass:{self.startAzCompass}\n' \
            f'Start Time:{self.startTime}\n' \
            f'Max Azimuth:{self.maxAz}\n' \
            f'Max Azimuth on Compass:{self.maxAzCompass}\n' \
            f'Max Time:{self.maxTime}\n' \
            f'End Azimuth:{self.endAz}\n' \
            f'End Azimuth on Compass:{self.endAzCompass}\n' \
            f'End Time:{self.endTime}\n' \
            f'Max visual magnitude:{self.mag}\n' \
            f'Total visible duration of this pass:{self.duration}\n' \
