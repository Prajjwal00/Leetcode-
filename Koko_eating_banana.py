# ques)-Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.
class Solution:
    def check(self,bananas, mid_val, h):
        time = 0;
        for i in range(len(bananas)):
            if (bananas[i] % mid_val != 0):
                time += bananas[i] // mid_val + 1;
            else:
       
      
                time += bananas[i] // mid_val
        if (time <= h):
            return True;
        else:
            return False;
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1;
        end = sorted(piles.copy(), reverse=True)[0]

        while (start < end):
            mid = start + (end - start) // 2;

        # Check if the mid(hours) is valid
            if (self.check(piles, mid, h) == True):
                end = mid;
            else:
                start = mid + 1;
        return end;   
