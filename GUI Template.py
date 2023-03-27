# Intro######################################
from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):  #creates window
  def __init__(self):
    EasyFrame.__init__(self)
    self.addLabel(text="Hello world!", row=0, column=0)#adds text to window

#pops window up
def main():
  LabelDemo().mainloop()

if __name__ == "__main__":
  main()
