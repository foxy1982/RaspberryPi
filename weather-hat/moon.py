def get_images():
  W = _white = (255, 255, 255)
  O = _nothing = (0,0,0)
      
  def _image_1():
    return [
    O, O, O, W, W, W, O, O,
    O, O, W, W, O, O, O, O,
    O, W, W, O, O, O, O, O,
    O, W, W, O, O, O, W, O,
    O, W, W, O, O, O, O, O,
    O, W, W, O, O, O, O, O,
    O, O, W, W, O, O, O, O,
    O, O, O, W, W, W, O, O
    ]

  def _image_2():
    return [
    O, O, O, W, W, W, O, O,
    O, O, W, W, O, O, O, O,
    O, W, W, O, O, O, W, O,
    O, W, W, O, O, W, W, W,
    O, W, W, O, O, O, W, O,
    O, W, W, O, O, O, O, O,
    O, O, W, W, O, O, O, O,
    O, O, O, W, W, W, O, O
    ]

  return [_image_1(), _image_2()]
