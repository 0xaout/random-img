from PIL import Image, ImageDraw
import random


class CoolImg:
    def __init__(self, x, y, bg_color):
        self.cube_number = random.randint(1,10)

        self.img = Image.new('RGB', (x, y), color=bg_color)
        self.draw = ImageDraw.Draw(self.img)

    def createRandom(self):
      
        # create random numbers of square with random colors and draw it on img

        for i in range(self.cube_number + 1):
            random_red = random.randint(0, 255)
            random_blue = random.randint(0, 255)
            random_green = random.randint(0, 255)

            random_x = random.randint(0, 9) * 10
            random_y = random.randint(0, 9) * 10

            

            self.draw.polygon([(random_x, random_y), (random_x + 10, random_y), (random_x + 10, random_y + 10), (random_x, random_y + 10)], fill=(random_red, random_green, random_blue))
    
    def create(self, number, size):

        z = 0

        for i in range(number + 1):
            z+=1
            random_red = random.randint(0, 256)
            random_blue = random.randint(0, 256)
            random_green = random.randint(0, 256)

            random_x = (random.randint(0, 9) * size)
            random_y = (random.randint(0, 9) * size)
            

           

            self.draw.rectangle([(random_x, random_y), (random_x + (size-1), random_y + (size-1))], fill=(random_red, random_green, random_blue), outline=None, width=0)



            print((random_x, random_y))

    # option pour générer une symetrie

    def sym(self): 
        pass

          


    def show(self):
        
        self.img.show()




img = CoolImg(500, 500, 'pink')
img.create(200, 50)
img.show()