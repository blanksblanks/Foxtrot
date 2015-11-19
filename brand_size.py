class BrandSize():
  def __init__(self, dict):
    self.brand_id = dict['BrandID']
    self.category_id = dict['CategoryID']
    self.fit = assign(dict, 'Fit')
    self.size_us = assign(dict, 'sizeUS')
    self.size_num = assign(dict, 'NumericSize')
    self.waist = assign(dict, 'NatWaist')
    self.hip = assign(dict, 'Hip')
    self.inseam = assign(dict, 'Inseam')
    self.bust = assign(dict, 'Bust')
    self.arm_length = assign(dict, 'Arm Length')
    self.torso = assign(dict, 'Torso')

  def assign(dict, key):
    return dict[key] if key in dict.keys() else -1
