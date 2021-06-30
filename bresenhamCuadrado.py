from PIL import Image, ImageDraw

def bresenhamLow(draw,x0,y0,x1,y1):
  dx = x1 - x0 #calcula tamanio de x (dx)
  dy = y1 - y0 #calcula tamanio de y (dy)
  
  yi = 1
  if dy < 0: #si dy es menor a 0
    yi = -1 
    dy = -dy #se decrementa 

  p = 2*dy - dx #calcula la variable p
  y = y0 #establece valor inicial de y

  for x in range(x0,x1): 
    draw.point((x,y),0)
    if p >= 0: 
        y = y + yi 
        p -= 2*dx 
        p += 2*dy 

def bresenhamHigh(draw,x0,y0,x1,y1):
  dx = x1 - x0 #calcula tamanio de x (dx)
  dy = y1 - y0 #calcula tamanio de y (dy)
  
  xi = 1
  if dx < 0: #si dx es menor a 0
    xi = -1
    dx = -dx #inverte dx

  p = 2*dx - dy
  x = x0 #establece valor inicaial de x

  for y in range(y0,y1): 
    draw.point((x,y),0) 
    if p >= 0: 
      x = x + xi
      p -= 2*dy 
    p += 2*dx 

def bresenham(draw,x0,y0,x1,y1):
    dx = x1 - x0 #calcula tamanio de x (dx)
    dy = y1 - y0 #calcula tamanoio de y (dy)
    
    if abs(dx) > abs(dy): #abs() retorna o valor absoluto
      bresenhamLow(draw,x0, y0, x1, y1)
    else:
      bresenhamHigh(draw,x0, y0, x1, y1)


im = Image.new('L',(100, 100),255)
draw = ImageDraw.Draw(im) 

              #x0,y0,x1,y1
bresenham(draw,10,10,80,40) #reta horizontal 
bresenham(draw,10,10,80,40) #reta horizontal 
bresenham(draw,10,10,10,80) #reta vertival 
bresenham(draw,10,80,80,80) #reta horizontal 
bresenham(draw,80,10,80,80) #reta vertival

im2 = im.resize((800,800)) #redimensiona la imagen de la biblioteca ImageDraw
im2.show() #exibi a imagem creada
im2.save("bresenham.png")