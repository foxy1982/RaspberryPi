def get_images():
  Y = yellow = (128, 128, 0)
  G = grey = (50, 50, 50)
  O = nothing = (0,0,0)
      
  def _image_1():
    return [
    Y, O, O, Y, O, O, O, Y,
    O, Y, O, O, O, O, Y, O,
    O, O, O, Y, Y, O, O, O,
    O, O, Y, Y, Y, Y, O, Y,
    Y, O, Y, Y, Y, Y, O, O,
    O, O, O, Y, Y, O, O, O,
    O, Y, O, O, O, O, Y, O,
    Y, O, O, O, Y, O, O, Y,
    ]

  def _image_2():
    return [
    Y, O, O, O, Y, O, O, Y,
    O, Y, O, O, O, O, Y, O,
    O, O, O, Y, Y, O, O, O,
    Y, O, Y, Y, Y, Y, O, O,
    O, O, Y, Y, Y, Y, O, Y,
    O, O, O, Y, Y, O, O, O,
    O, Y, O, O, O, O, Y, O,
    Y, O, O, Y, O, O, O, Y,
    ]

  return [_image_1(), _image_2()]
