from PIL import Image, ImageDraw
import random


class CoolImg:
    def __init__(self, x, y, bg_color):
        self.cube_number = random.randint(1,10)

        self.img = Image.new('RGB', (x, y), color=bg_color)
        self.draw = ImageDraw.Draw(self.img)
        self.x = x


    # création d'une image avec un nombre de carré aléatoire et de couleurs aléatoires
    def createRandom(self):
        for i in range(self.cube_number + 1):
            random_red = random.randint(0, 255)
            random_blue = random.randint(0, 255)
            random_green = random.randint(0, 255)

            random_x = random.randint(0, 9) * 10
            random_y = random.randint(0, 9) * 10

            self.draw.polygon([(random_x, random_y), (random_x + 10, random_y), (random_x + 10, random_y + 10), (random_x, random_y + 10)], fill=(random_red, random_green, random_blue))
    
    # crée une image avec un nombre de carré défini avec une taille définie
    def create(self, number, size):
        for i in range(number + 1):
            random_red = random.randint(0, 256)
            random_blue = random.randint(0, 256)
            random_green = random.randint(0, 256)

            rgb = (random_red, random_green, random_blue)

            square_width = self.x / size
            maxi = size*square_width - square_width

            random_x = (random.randint(0, (size - 1)) * square_width)
            random_y = (random.randint(0, (size - 1)) * square_width)        

            self.draw.rectangle([(random_x, random_y), (random_x + (square_width-1), random_y + (square_width-1))], fill=rgb, outline=None, width=0)

    # générer une image avec une symetrie verticale
    def ySym(self, number, size, color=None): 

        symetry = []
        square_width = self.x / size
        maxi = size*square_width - square_width
             
        for i in range(number + 1):
            random_red = random.randint(0, 256)
            random_blue = random.randint(0, 256)
            random_green = random.randint(0, 256)

            if color == None:
                rgb = (random_red, random_green, random_blue)
            else:
                rgb = color

            random_x = (random.randint(0, (int(size / 2))) * square_width)
            random_y = (random.randint(0, (size - 1)) * square_width)

            symetry.append((random_x, random_y))
    
            self.draw.rectangle([(random_x, random_y), (random_x + (square_width-1), random_y + (square_width-1))], fill=rgb, outline=None, width=0)

            if color == None:
                random_red = random.randint(0, 256)
                random_blue = random.randint(0, 256)
                random_green = random.randint(0, 256)

                rgb = (random_red, random_green, random_blue)
            else:
                rgb = color

            self.draw.rectangle([(maxi - random_x, random_y), (maxi - random_x + (square_width-1), random_y + (square_width-1))], fill=rgb, outline=None, width=0)

    # générer une image avec une symetrie horizontale
    def xSym(self, number, size, color=None): 

        symetry = []
        square_width = self.x / size
        maxi = size*square_width - square_width
        
        for i in range(number + 1):
            random_red = random.randint(0, 256)
            random_blue = random.randint(0, 256)
            random_green = random.randint(0, 256)

            if color == None:
                rgb = (random_red, random_green, random_blue)
            else:
                rgb = color

            random_x = (random.randint(0, (size - 1)) * square_width)
            random_y = (random.randint(0, (int(size / 2))) * square_width)

            symetry.append((random_x, random_y))

            self.draw.rectangle([(random_x, random_y), (random_x + (square_width-1), random_y + (square_width-1))], fill=rgb, outline=None, width=0)

            if color == None:
                random_red = random.randint(0, 256)
                random_blue = random.randint(0, 256)
                random_green = random.randint(0, 256)

                rgb = (random_red, random_green, random_blue)
            else:
                rgb = color

            self.draw.rectangle([(random_x, maxi - random_y), (random_x + (square_width-1), maxi -  random_y + (square_width-1))], fill=rgb, outline=None, width=0)


    def show(self):
        self.img.show()
        self.img.save("test.png")




img = CoolImg(500, 500, 'white')
img.ySym(10, 5, 'black')
img.show()