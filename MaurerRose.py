import pygame;
import math;
import pygame_widgets;
WIDTH: int = 800;
HEIGHT: int = 800;
BLUE = (0,0,255);
GREEN = (0,255,0);
screen = pygame.display.set_mode((WIDTH,HEIGHT));
size = 250;
pygame.init();
n = 2
d = 39
Nslider = pygame_widgets.Slider(screen, 50, 100, 120, 20, min=0, max=120, step=1, initial = n)
Kslider = pygame_widgets.Slider(screen, 50, 150, 120, 20, min=0, max=120, step=1, initial = d)
font = pygame.font.Font('freesansbold.ttf', 20) 
prevX = 0 + WIDTH//2
prevY = 0 + HEIGHT // 2
list =  [];
while True:
	screen.fill([255,255,255]);
	events = pygame.event.get()
	Nslider.listen(events);
	Nslider.draw()
	Kslider.listen(events);
	Kslider.draw()
	nText = font.render("N = " + str(n), True, GREEN) 
	dText = font.render("D = " + str(d), True, GREEN) 
	nTextRect = nText.get_rect()  
	dTextRect = dText.get_rect()  
	nTextRect.center = (230, 110) 
	dTextRect.center = (230, 160) 
	screen.blit(nText, nTextRect)
	screen.blit(dText, dTextRect)
	n = Nslider.getValue();
	d = Kslider.getValue();
	for theta in range(361):
		k = theta * d * math.pi / 180;
		r = size * math.sin(n * k);
		list.append((prevX,prevY));
		x = int(r * math.cos(k)) + WIDTH//2;
		y = -1 * int(r * math.sin(k)) + HEIGHT//2 ;
		pygame.draw.line(screen, GREEN, (list.pop()), (x,y), 1);
		prevX = x;
		prevY = y;		
		pygame.event.pump();
	for theta in range(361):
		k = theta * math.pi / 180;
		r = size * math.sin(n * k);
		list.append((prevX,prevY));
		x = int(r * math.cos(k)) + WIDTH//2;
		y = -1 * int(r * math.sin(k)) + HEIGHT//2;
		pygame.draw.line(screen, BLUE, (list.pop()), (x,y), 1);
		prevX = x;
		prevY = y;		
	
	pygame.display.update();
