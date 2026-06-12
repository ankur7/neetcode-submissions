class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions with speeds and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_max_time = 0.0
        
        for p, s in cars:
            time = (target - p) / s
            
            # If this car takes MORE time than the fleet in front of it,
            # it cannot catch up. It starts a new fleet.
            if time > current_max_time:
                fleets += 1
                current_max_time = time # This car is now the leader of the new fleet
                
        return fleets