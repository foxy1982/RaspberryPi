def get_images():
  G = _grey = (56,56,56)
  W = _white = (255,255,255)

  def _image_1():
    return [
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, W, W, G, G, G,
    G, G, W, G, G, W, W, G,
    G, W, G, G, W, G, G, W,
    G, G, W, W, W, W, W, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G    
    ]

  return [_image_1()]
