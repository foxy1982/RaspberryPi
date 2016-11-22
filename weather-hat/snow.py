def get_images():
  X = _nothing = (0,0,0)
  G = _grey = (128,128,128)
  W = _white = (255,255,255)

  def _image_1():
    return [
    X, X, X, G, G, X, X, X,
    X, X, G, X, X, G, G, X,
    X, G, X, X, G, X, X, G,
    X, W, G, G, G, G, G, X,
    X, X, W, X, X, W, X, X,
    X, X, X, X, X, X, W, X,
    X, W, X, X, W, X, X, X,
    X, X, X, W, X, X, X, W    
    ]

  def _image_2():
    return [
    X, X, X, G, G, X, X, X,
    X, X, G, X, X, G, G, X,
    X, G, X, X, G, X, X, G,
    X, X, G, G, G, G, G, W,
    X, W, X, X, X, X, X, X,
    X, X, W, X, X, W, X, X,
    X, X, X, X, X, X, W, X,
    X, W, X, X, W, X, X, X  
    ]

  return [_image_1(), _image_2()]
