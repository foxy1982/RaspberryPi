def get_images():
  O = _nothing = (0,0,0)
  G = _grey = (128,128,128)

  def _image_1():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, O, O, G, G, O,
    O, G, O, O, G, O, O, G,
    O, O, G, G, G, G, G, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O    
    ]

  def _image_2():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, G, G, O, O,
    O, O, O, G, O, O, G, G,
    G, O, G, O, O, G, O, O,
    O, O, O, G, G, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O   
    ]

  def _image_3():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, G, G, O,
    G, O, O, O, G, O, O, G,
    O, G, O, G, O, O, G, O,
    G, O, O, O, G, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

  def _image_4():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, G, G,
    G, G, O, O, O, G, O, O,
    O, O, G, O, G, O, O, G,
    G, G, O, O, O, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

  def _image_5():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    G, O, O, O, O, O, O, G,
    O, G, G, O, O, O, G, O,
    G, O, O, G, O, G, O, O,
    G, G, G, O, O, O, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

  def _image_6():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    G, G, O, O, O, O, O, O,
    O, O, G, G, O, O, O, G,
    O, G, O, O, G, O, G, O,
    G, G, G, G, O, O, O, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

  def _image_7():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, G, G, O, O, O, O, O,
    G, O, O, G, G, O, O, O,
    O, O, G, O, O, G, O, G,
    G, G, G, G, G, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

  def _image_8():
    return [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, G, G, O, O, O, O,
    O, G, O, O, G, G, O, O,
    G, O, O, G, O, O, G, O,
    O, G, G, G, G, G, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

  return [_image_1(), _image_2(), _image_3(), _image_4(), _image_5(), _image_6(), _image_7(), _image_8()]
