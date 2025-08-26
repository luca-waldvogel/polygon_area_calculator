class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            for j in range(self.width):
                picture += '*'
                if j == self.width - 1:
                    picture += '\n'
        return picture

    def get_amount_inside(self, other):
        fit_width = self.width // other.width
        fit_height = self.height // other.height
        return fit_width * fit_height
    
    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.height = side
        self.width = side
    
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.width})'


rect = Rectangle(16, 8)
rect2 = Rectangle(4, 4)
print(rect.get_picture())
print(rect)
print()

sq = Square(4)
sq.set_side(5)
print(sq.get_picture())
print(sq)