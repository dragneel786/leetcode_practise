class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        min_time, max_time = 0, 0
        count = 0
        while(max_time < time):
            for clip in clips:
                start, end = clip
                if(start <= min_time and end > max_time):
                    max_time = end
            
            if(min_time == max_time):
                return -1
            min_time = max_time
            count += 1
        return count
        