
'''
Description
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
Example
Example 1:
Input: "GGLRRRGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
Repeat these instructions and the robot will cycle through this path。
Example 2:
Input: "GG"
Output: false
Explanation: The robot has been moving north.
'''


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # method 1 loop 4 times the instrctions, if back to (0,0) then True
        # method 2 only loop 1 time, two situations
        # back to (0, 0), then True
        # not back to (0,0)
        # not face North, then True
        # face North, then False
        # use method 2 here
        # North, East, South, West
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        # facing North
        face_idx = 0

        for i in instructions:
            if i == "L":
                face_idx = (face_idx + 3) % 4
            elif i == "R":
                face_idx = (face_idx + 1) % 4
            else:
                x += direction[face_idx][0]
                y += direction[face_idx][1]

        return (x, y) == (0, 0) or face_idx != 0
