import random
from main import BLUE

class letters: 
  def __init__(self, color):
    wordbank = ["blaze", 
      "crisp", 
      "swing", 
      "chair", 
      "bread", 
      "video", 
      "world", 
      "blink", 
      "coder"]
    self.Wordbank = wordbank
    self.Color = color

  def getrandom(self):
    current = random.choice(self.Wordbank)
    return current

letter = letters(BLUE)
print(letter.getrandom())

