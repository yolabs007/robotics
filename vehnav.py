"""
Sample Python/Pygame based control using keyboard 
Yolabs Robotics/Programming Classes
https://yolabs.in/ changed 
"""
#>>>>>>>>>>>>>>>>> import gpio, time, pygame and picamera
import RPi.GPIO as GPIO
from time import sleep 
import pygame
#import picamera

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 
# Define some colors that you will use while drawing your screen 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
# Declaring pins as PWM for speed control 
fl = GPIO.PWM(7,50) # forward for left motors 
bl= GPIO.PWM(11,50) # backward for left motors 
fr = GPIO.PWM(13,50) # forward for right motors 
br = GPIO.PWM(15,50) # backward for right motors 
# starting the pins 
fl.start(0)
bl.start(0)
fr.start(0)
br.start(0)
 
# define vehicle control
direction  = 0 #   1 - forward, 2 - right, 3 - backward, 4- left 
duty = 50    # vehicle Speed 
def veh_control():
    # forward direction 
    if direction==1:
    
        fl.ChangeDutyCycle(duty)
        fr.ChangeDutyCycle(duty)
        bl.ChangeDutyCycle(0)
        br.ChangeDutyCycle(0)
        print("speed-->", duty)
    # to move backward    
    elif direction==2:
        
        fl.ChangeDutyCycle(0)
        fr.ChangeDutyCycle(0)
        bl.ChangeDutyCycle(duty)
        br.ChangeDutyCycle(duty)
        print("speed-->", duty)    
          
     # to move left    
   
    elif direction==3:
        fl.ChangeDutyCycle(0)
        fr.ChangeDutyCycle(duty)
        bl.ChangeDutyCycle(duty)
        br.ChangeDutyCycle(0)
        print("speed-->", duty)
     
     # to move right     

    elif direction==4:
        fl.ChangeDutyCycle(duty)
        fr.ChangeDutyCycle(0)
        bl.ChangeDutyCycle(0)
        br.ChangeDutyCycle(duty)
        print("speed-->", duty)   
  # to Stop the Vehicle 
    elif direction==0: 
        fl.ChangeDutyCycle(0)
        fr.ChangeDutyCycle(0)
        bl.ChangeDutyCycle(0)
        br.ChangeDutyCycle(0)
        print("speed--> 0")
   
# >>>> Set your Camera <<<<<<<<<
#camera = picamera.PiCamera() # bring your camera
#camera.rotation = 180

#camera.start_preview(fullscreen = False, window = (600,400,600,300)) # first and second for position & third and fourth value for size 

#>>>>>>>>>>>>>>>>>>>>>


# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_UP:
                direction  = 1
            elif event.key == pygame.K_DOWN:
                direction  = 2
            elif event.key == pygame.K_RIGHT:
                direction  = 3
            elif event.key == pygame.K_LEFT:
                direction  = 4
            elif event.key == pygame.K_RETURN:
                direction = 0
            if event.key == pygame.K_i and duty<100:
                duty  = duty+2
            elif event.key == pygame.K_d and duty>50:
                duty  = duty-2
            elif event.key==pygame.K_i and event.key==pygame.K_d:
                duty = duty    
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    # --- Game Logic
 
    # Move the object according to the speed vector.
    #x_coord = x_coord + x_speed
    #y_coord = y_coord + y_speed
 
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    print("speed----->", duty)
    #draw_stick_figure(screen, x_coord, y_coord)
    veh_control()
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(20)
 
# Close the window and quit.
fl.stop()
bl.stop()
fr.stop()
br.stop()
#camera.stop_preview()   
GPIO.cleanup()
pygame.quit()
