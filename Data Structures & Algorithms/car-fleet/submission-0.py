class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedmap = {}
        
        for i in range(len(position)):
            speedmap[position[i]] = speed[i]

        position.sort()
        stack = []

        for i in range(len(position)-1, -1, -1):
            remaining = target - position[i]
            time = remaining/speedmap[position[i]]

            if not stack:
                stack.append(time)
            else:
                fleet_time = stack[-1]
                if time > fleet_time:
                    stack.append(time)

        return len(stack)
