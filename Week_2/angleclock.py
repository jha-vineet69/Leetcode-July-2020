class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 0.5 * (60*hour + minutes)
        minute_angle = 6 * minutes
        return min(abs(hour_angle-minute_angle), 360-abs(hour_angle-minute_angle))
        
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(0.5 * (60*hour - 11*minutes))
        return min(angle, 360-angle)