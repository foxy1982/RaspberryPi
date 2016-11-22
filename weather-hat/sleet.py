def get_images():
  X = _nothing = (0,0,0)
  G = _grey = (128,128,128)
  B = _blue = (0,0,255)
  W = _white = (255,255,255)

  def _image_1():
    return [
    X, X, X, G, G, X, X, X,
    X, X, G, X, X, G, G, X,
    X, G, X, X, G, X, X, G,
    X, B, G, G, G, G, G, B,
    X, X, W, B, X, X, X, B,
    X, X, X, B, X, B, W, X,
    X, B, X, X, W, B, X, X,
    X, B, W, X, X, X, X, B    
    ]

  def _image_2():
    return [
    X, X, X, G, G, X, X, X,
    X, X, G, X, X, G, G, X,
    X, G, X, X, G, X, X, G,
    X, X, G, G, G, G, G, X,
    X, B, X, X, W, B, X, X,
    X, B, W, X, X, X, X, B,
    X, X, X, B, X, X, W, B,
    X, X, X, B, W, B, X, X  
    ]

  return [_image_1(), _image_2()]
