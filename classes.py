class Engine:
  _cyclinders: int
  def __init__(self, cyclinders: int) -> None:
      self._cyclinders = cyclinders

  def accelerate(self):
    if(self._cyclinders > 4):
      print('rem rem rem')
    else:
      print('pooooo poooooo')

class Vehicle:
  _engine: Engine
  def __init__(self, engine: Engine) -> None:
    self._engine = engine

  def accelerate(self):
    self._engine.accelerate()

class Honda(Vehicle):
  def __init__(self) -> None:
      super().__init__(Engine(4))
      print('building a HONDA')

  def accelerate(self):
      #vtec
      print('bang! bang! bang!')
      return super().accelerate()

class Nissan(Vehicle):
  def __init__(self) -> None:
      super().__init__(Engine(6))
      print('building a NISSAN')


class Toyota(Vehicle):
  def __init__(self) -> None:
      super().__init__(Engine(4))
      print('building a TOYOTA')

nissan = Nissan()
nissan.accelerate()

honda = Honda()
honda.accelerate()

toyota = Toyota()
toyota.accelerate()

input()