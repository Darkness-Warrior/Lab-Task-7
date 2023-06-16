class Vectors:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def __add__(self, other):  # "other" реально очень удобный
        return Vectors(self.x1 + other.x1, self.y1 + other.y1, self.z1 + other.z1,
                       self.x2 + other.x2, self.y2 + other.y2, self.z2 + other.z2)

    def __sub__(self, other):
        return Vectors(self.x1 - other.x1, self.y1 - other.y1, self.z1 - other.z1,
                       self.x2 - other.x2, self.y2 - other.y2, self.z2 - other.z2)

    def dot(self, other):
        return (self.x2 - self.x1) * (other.x2 - other.x1) + (self.y2 - self.y1) * (other.y2 - other.y1) + (
                       self.z2 - self.z1) * (other.z2 - other.z1)

    def length(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2 + (self.z2 - self.z1) ** 2) ** 0.5

    def cos_angle(self, other):
        return self.dot(other) / (self.length() * other.length())