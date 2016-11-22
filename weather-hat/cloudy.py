def get_images():
  X = _nothing = (0,0,0)
  G = _grey = (128,128,128)

  def _image_1():
    return [
    X, X, G, G, X, X, X, X,
    X, G, X, X, G, G, X, X,
    G, X, X, G, X, G, G, G,    
    X, G, G, G, G, X, X, X,
    X, X, X, G, X, X, G, G,
    X, X, G, X, X, G, X, X,
    X, X, X, G, G, G, G, G,
    X, X, X, X, X, X, X, X
    ]

  return [_image_1()]
