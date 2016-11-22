def get_images():
  Y = _yellow = (128, 128, 0)
  G = _grey = (50, 50, 50)
  X = _nothing = (0,0,0)

  def _image_1():
    return [
    X, X, X, G, G, X, X, X,
    X, X, G, X, X, G, G, X,
    X, G, X, X, G, X, X, G,
    X, X, G, G, G, G, G, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X    
    ]

  def _image_2():
    return [
    X, X, X, G, G, X, X, X,
    X, X, G, X, X, G, G, X,
    X, G, X, X, G, X, X, G,
    X, X, G, G, G, G, G, X,
    X, X, X, X, Y, X, X, X,
    X, X, X, Y, Y, Y, X, X,
    X, X, X, Y, X, X, X, X,
    X, X, Y, X, Y, X, X, X  
    ]

  return [_image_1(), _image_2()]
