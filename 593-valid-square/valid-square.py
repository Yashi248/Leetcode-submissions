class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(pointA,pointB):
            return (pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2
        
        SqDist = [
            dist(p1,p2),
            dist(p2,p3),
            dist(p3,p4),
            dist(p4,p1),
            dist(p1,p3),
            dist(p2,p4)
        ]

        SqDist.sort()

        if SqDist[0]==SqDist[1]==SqDist[2]==SqDist[3] > 0 and SqDist[4]==SqDist[5]:
            return True
        
        return False