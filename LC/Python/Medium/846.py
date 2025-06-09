class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        
        count = Counter(hand)
        hand.sort()
        
        for i in range(len(hand)):
            curr_num = hand[i]
            if curr_num not in count:
                continue

            for j in range(groupSize):
                if curr_num + j not in count:
                    return False
                
                count[curr_num+j] -= 1
                
                if count[curr_num+j] == 0:
                    del count[curr_num+j]
        
        return True