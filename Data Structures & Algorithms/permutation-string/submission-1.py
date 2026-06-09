from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_size = len(s1)
        s1_count = Counter(s1)
        # Initialize window with the first len(s1) characters of s2
        window_count = Counter(s2[:w_size])
        
        # Check the very first window
        if s1_count == window_count:
            return True
            
        # Slide the window across s2
        for r in range(w_size, len(s2)):
            # Add the new character entering the window
            window_count[s2[r]] += 1
            
            # Remove the old character leaving the window
            l_char = s2[r - w_size]
            window_count[l_char] -= 1
            if window_count[l_char] == 0:
                del window_count[l_char] # Clean up 0 counts so dictionary matches s1_count
                
            # Direct comparison
            if window_count == s1_count:
                return True
                
        return False