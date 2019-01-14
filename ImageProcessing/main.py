
from imageRead import ImageRead as Reader
from component import component as Identify

image = Reader("img/Sample/read.png").get()

Identify(image)

