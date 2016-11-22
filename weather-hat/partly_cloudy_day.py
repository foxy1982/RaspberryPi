def get_images():
  O = _nothing = (0,0,0)
  G = _grey = (128,128,128)
  Y = _yellow = (128,128,0)

  def _image_1():
    return [
    O, O, O, O, O, O, O, O,
    O, O, Y, Y, O, O, O, O,
    O, Y, Y, Y, Y, O, O, O,
    O, Y, Y, G, G, O, O, O,
    O, O, G, O, O, G, G, O,
    O, G, O, O, G, O, O, G,
    O, O, G, G, G, G, G, O,
    O, O, O, O, O, O, O, O    
    ]

  def _image_2():
    return [
    Y, O, O, O, O, Y, O, O,
    O, O, Y, Y, O, O, O, O,
    O, Y, Y, Y, Y, O, Y, Y,
    O, Y, Y, G, G, O, O, O,
    O, O, G, O, O, G, G, O,
    Y, G, O, O, G, O, O, G,
    O, O, G, G, G, G, G, O,
    O, O, O, O, O, O, O, O    
    ]

  return [_image_1(), _image_2()]
