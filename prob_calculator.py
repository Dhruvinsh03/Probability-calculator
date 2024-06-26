import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**balls):
    self.contents=[]
    for colour,count in balls.items():
      for i in range(count):
        self.contents.append(colour)
  def draw(self,num):
    drawn_balls=random.sample(self.contents,min(num,len(self.contents)))
    for ball in drawn_balls:
      self.contents.remove(ball)
    return drawn_balls  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes=0
  for i in range(num_experiments):
    hat_copy=copy.deepcopy(hat)
    drawn_balls=hat_copy.draw(num_balls_drawn)
    drawn_balls_count={}
    for ball in drawn_balls:
      drawn_balls_count[ball]=drawn_balls_count.get(ball,0)+1
    success=True
    for colour,count in expected_balls.items():
      if drawn_balls_count.get(colour,0)<count:
        success=False
        break
    if success:
      successes+=1
  return successes/num_experiments
  
