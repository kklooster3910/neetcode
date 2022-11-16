from collections import deque
"""
Given a stream of integers and a window size, calculate the moving average of all integers in the array

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
"""


"""
queue = deque([])
queue.popleft()
queue.pop()
queue.appendleft()
queue.append()
"""
movingAverage = new MovingAverage(3) # -> []
movingAverage.next(1); # return 1.0 = 1 / 1
movingAverage.next(10); # return 5.5 = (1 + 10) / 2
movingAverage.next(3); # return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); # return 6.0 = (10 + 3 + 5) / 3

# Initializing class, we want a create of a deque of given size
#   Next method each time its run
  # Checks deque size
    #Size is max, then shift()
  #Add new element to end 
  # Return the average of the deque elements

class MovingAverage:

    def __init__(self, size: int):
      self.queue = deque([])
      self.size = size
      self.currSize = 0

    def next(self, val: int) -> float:

      if self.currSize == self.size:
        self.queue.popleft()
      else:
        self.currSize += 1 
      self.queue.append(val)
      return sum(self.queue) / self.currSize