class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = []
        for row in range(self.height):
            for col in range(self.width):
                picture.append("*")
        picture.append("\n")
        return "".join(picture) + "\n"

    # TODO: Complete after creating the Square class
    def get_amount_inside(self, shape):
        pass

# TODO: Create Square class (Rectangle child class)
class Square:
    pass