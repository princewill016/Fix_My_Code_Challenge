ass square():
    def __init__(self, *args, **kwargs):
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
    
    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width
    
    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)
    
    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
