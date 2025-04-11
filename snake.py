import pygame,sys,random
from pygame import mixer
pygame.init()
w,h=600,600
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('snake and pink apple game ')
clock=pygame.time.Clock()
a=mixer.Sound(r'C:\my game\gallary\audio\jungle.mp3')
b=mixer.Sound(r'C:\my game\gallary\audio\bite.mp3')
a.play(-1)
loop=True
snakex=200
snakey=200
foodx=random.randint(50,500)
foody=random.randint(50,500)
size=21
snakex_v=0
snakey_v=0
score=0
style=pygame.font.Font(None,68)
def font(text,color,x,y):
    img=style.render(text,False,color)
    screen.blit(img,(x,y)) 
list=[[snakex,snakey]]
l=1
def plot(screen,color,list1,size):
     for x,y in list:
         pygame.draw.rect(screen,'red',(x,y,size,size))     
game=True    
while loop:
        screen.fill('orange')
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                loop=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                      snakey_v=-10
                      snakex_v=0
                if event.key==pygame.K_DOWN:
                       snakey_v=10
                       snakex_v=0
                if event.key==pygame.K_RIGHT:
                      snakey_v=0
                      snakex_v=10
                if event.key==pygame.K_LEFT:
                      snakey_v=0
                      snakex_v=-10
            if event.type==pygame.MOUSEBUTTONDOWN:
                 game=True
                 snakex=200
                 snakey=200 
                 score=0
                 snakex_v=0
                 snakey_v=0 
                 l=0
                 list=[[snakex,snakey]]       
        if game:              
            snakex+=snakex_v
            snakey+=snakey_v
            list.append([snakex,snakey]) 
            if len(list)>l: 
                    
                  del list[0]                              
            pygame.draw.rect(screen,'red',(snakex,snakey,size,size))
            pygame.draw.rect(screen,'pink',(foodx,foody,size,size))
            if abs(snakex-foodx)<10 and abs(snakey-foody)<10:
                foodx=random.randint(50,500)
                foody=random.randint(50,500)
                score+=1
                l+=1   
            plot(screen,'red',list,size)    
            font(f'score is {score}','black',5,5)
            if snakex>=600 or snakex<=0 or snakey>=600 or snakey<=0:
              game=False
              b.play()
        else: 
             screen.fill('orange')
             font(f'score is {score}','black',50,5)
             font(f'tap mouse to play  again','black',50,50)
        pygame.display.update()
        clock.tick(30)
pygame.quit()
                    


