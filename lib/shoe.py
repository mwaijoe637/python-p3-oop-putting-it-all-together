# lib/shoe.py

class Shoe:
    def __init__(self, brand, size, color, material):
        self.brand = brand
        self.size = size
        self.color = color
        self.material = material
        self.is_worn = False
    
    def wear(self):
        self.is_worn = True
    
    def remove(self):
        self.is_worn = False
    
    def __str__(self):
        return f"{self.color} {self.brand} shoe, size {self.size}, made of {self.material}"
    
    # Properties using the property() function
    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        if not brand:
            raise ValueError("Brand cannot be empty")
        self._brand = brand
    
    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if size <= 0:
            raise ValueError("Size must be a positive number")
        self._size = size
    
    size = property(get_size, set_size)

    def get_color(self):
        return self._color
    
    def set_color(self, color):
        if not color:
            raise ValueError("Color cannot be empty")
        self._color = color
    
    color = property(get_color, set_color)

    def get_material(self):
        return self._material
    
    def set_material(self, material):
        if not material:
            raise ValueError("Material cannot be empty")
        self._material = material
    
    material = property(get_material, set_material)
