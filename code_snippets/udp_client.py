import pygame
import socket

IP = "192.168.8.1"	# Beagle Bone AP Default Gateway IP
PORT = 6969		# Beagle Bone DSTR Server Port

pygame.init()

display_width = 300
display_height = 300

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MXET Controller')

white = (255,255,255)

clock = pygame.time.Clock()

while True:

	key = b""
	
	for event in pygame.event.get():
	
		if event.type == pygame.KEYDOWN:
		
			if event.key == pygame.K_LEFT:
				key = b"0"
				
			elif event.key == pygame.K_RIGHT:
				key = b"1"
				
			elif event.key == pygame.K_UP:
				key = b"2"
				
			elif event.key == pygame.K_DOWN:
				key = b"3"
				
			elif event.key == pygame.K_RSHIFT:
				key = b"4"
				
			elif event.key == pygame.K_SPACE:
				key = b"5"
				
			elif event.key == pygame.K_ESCAPE:
				print("Exiting!")
				key = b"4"
				clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				clientSock.sendto(key, (IP, PORT))
				pygame.quit()
				exit()
			
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				key = b"4"
		
	gameDisplay.fill(white)
	
	pygame.display.update()
	clock.tick(60)
	
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	clientSock.sendto(key, (IP, PORT))
	
pygame.quit()
quit()