from rembg import remove
from PIL import Image

img = Image.open('papagaio.jpg')

img2 = remove(img)

img2.save('papagaio_sem_bg.png')