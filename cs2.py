import pygame
import time
import random,sys
import pygame.sprite as Sprite

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR=pygame.Color(0,0,128)
pygame.init()
aite=0

class BaseItem(Sprite.Sprite):
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

# 主
class MainGame():
    window = None
    my_play=None
    enemyplayList=[]
    enemyplayCount=5
    #存储我方子弹的列表
    myBulletList=[]
   
    enemyBulletList=[]
    explodeList=[]
    # 加载主窗口
    pygame.display.init()  # 初始化窗口

    def __init__(self):
        pass
    
    # 开始游戏
    def startGame(self):
        
        # 加载主窗口
        #pygame.display.init()  # 初始化窗口
        # 设置窗口的大小
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption('反恐精英')

        # 加载背景图像
        background_img = pygame.image.load("bg.png")
        background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # 初始化我方战士
        MainGame.my_play=play(650,650)
        self.createEnemyplay()
        self.my_play.displayplay()
        clock = pygame.time.Clock()
        while True:
            MainGame.window.fill(BG_COLOR)
            MainGame.window.blit(background, (0, 0))
            clock.tick(60)
            
            self.handleEvent()  # 处理事件
            MainGame.window.blit(self.getTextSuface("敌方战士剩余数量：%d 战士使用的枪械:%s" % (len(MainGame.enemyplayList), qiang[alit])), (10, 10))
 

            #显示战士
            if MainGame.my_play and MainGame.my_play.live:
                MainGame.my_play.displayplay()
            else:
                del MainGame.my_play
                MainGame.my_play=None
            self.blitEnemyplay()
            # 循环遍历来显示我方战士的子弹
            self.blitMyBullet()
            self.blitEnemyBullet()
            self.blitExplode()
            if MainGame.my_play and MainGame.my_play.live:
                if not MainGame.my_play.stop:
                    MainGame.my_play.move()
            
            pygame.display.update()
            
            
    def createEnemyplay(self):
        top=100
        for i in range(MainGame.enemyplayCount):
            left=random.randint(0,900)
            speed=random.randint(1,4)
            enemy=Enemyplay(left,top,speed)
            MainGame.enemyplayList.append(enemy)
    #循环遍历敌人列表
    def blitEnemyplay(self):
        for enemyplay in MainGame.enemyplayList:
            if enemyplay.live:
                enemyplay.displayplay()
                enemyplay.randMove()
                enemyBullet=enemyplay.shot()
                if enemyBullet:
                    MainGame.enemyBulletList.append(enemyBullet)
            else:
                MainGame.enemyplayList.remove(enemyplay)
            

    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            if myBullet.live:

                myBullet.displayBullet()
                myBullet.move()
                myBullet.myBullt_hit_enemyplay()
            else:
                MainGame.myBulletList.remove(myBullet)
    def blitExplode(self):
        for explode in MainGame.explodeList:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.explodeList.remove(explode)
    def blitEnemyBullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            if enemyBullet.live:
                enemyBullet.displayBullet()
                enemyBullet.move()
                # 调用敌方子弹与我方战士碰撞的方法
                enemyBullet.enemyBullet_hit_myplay()

            else:
                MainGame.enemyBulletList.remove(enemyBullet)
        

    #结束游戏
    def endGame(self):
        print('谢谢使用，欢迎您下次使用')
        exit()  #退出
    #左上角
    def getTextSuface(self,text):
        pygame.font.init()
        font=pygame.font.SysFont('kaiti',18)
        #文字信息
        textSurface=font.render(text,True,TEXT_COLOR)
        return textSurface

    # 事件处理
    def handleEvent(self):
        
        
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            #键盘控制游戏-----上下左右
            if event.type==pygame.KEYDOWN:
               if MainGame.my_play and MainGame.my_play.live:
                    if event.key==pygame.K_LEFT:
                        MainGame.my_play.direction='L'
                        #MainGame.my_play.move()
                        MainGame.my_play.stop=False
                        print('按下左键')

                    elif event.key==pygame.K_RIGHT:
                        MainGame.my_play.direction='R'
                        #MainGame.my_play.move()
                        MainGame.my_play.stop=False
                        print('按下右键')
                    elif event.key==pygame.K_UP:
                        MainGame.my_play.direction='U'
                        #MainGame.my_play.move()
                        MainGame.my_play.stop=False
                        print('按下上键')
                    elif event.key==pygame.K_DOWN:
                        MainGame.my_play.direction='D'
                        #MainGame.my_tank.move()
                        MainGame.my_play.stop=False
                        print('按下下键')
                        
                    


                    elif event.key==pygame.K_SPACE:
                        
                        print('玩家使用了'+qiang[alit]+'发射子弹')

                        #创建子弹   我方战士发射的子弹
                        if len(MainGame.myBulletList)<3:
                            myBullet=Bullet(MainGame.my_play)
                            MainGame.myBulletList.append(myBullet)
       
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    if MainGame.my_play and MainGame.my_play.live:
                        MainGame.my_play.stop=True

image = pygame.image.load("player.png")
# 缩小图像
scaled_image = pygame.transform.scale(image, (85, 85))

image2 = pygame.image.load("player2.png")
scaled_image2 = pygame.transform.scale(image2, (85, 85))        

image3 = pygame.image.load("enemy.png")
scaled_image3= pygame.transform.scale(image3, (120, 130)) 

image5 = pygame.image.load("enemy2.png")
scaled_image5= pygame.transform.scale(image5, (120, 130))

image4 = pygame.image.load("bullet.png")
scaled_image4= pygame.transform.scale(image4, (40, 40)) 
# 战士类
class play(BaseItem):
    def __init__(self,left,top):
        self.images={'U':scaled_image2,
                     'D':scaled_image,
                     'R':scaled_image2,
                     'L':scaled_image}
        self.direction='L'
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.speed=5   #移动的快慢
        self.stop=True
        self.live=True
        self.blood=100   # 血量

    # 移动
    def move(self):
        if self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
        elif self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
        elif self.direction=='D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top+=self.speed
        elif self.direction=='R':
            if self.rect.left+self.rect.width<SCREEN_WIDTH:
                self.rect.left+=self.speed

    # 射击
    def shot(self):
        return Bullet(self)

    # 显示战士
    def displayplay(self):
        self.image=self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)
         # 显示血量
        
        pygame.font.init()
        font=pygame.font.SysFont('kaiti',18)
        #文字信息
        #textSurface=font.render('血量',True,TEXT_COLOR)
        text=font.render('血量: {}'.format(self.blood), True, (255,255,255))
        MainGame.window.blit(text, (self.rect.left, self.rect.top - 20))
# 敌方战士
class Enemyplay(play):
    
    def __init__(self,left,top,speed):
        # 调用父类的初始化方法
        super(Enemyplay,self).__init__(left,top)
        super()
        self.images={
            'U':scaled_image3,
            'D':scaled_image5,
            'L':scaled_image3,
            'R':scaled_image5
         }
        self.direction=self.ranDirection()
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.speed=speed
        self.flag=True
        #步数变量
        self.step=120
    def displayplay(self):
        self.image=self.images[self.direction]

        MainGame.window.blit(self.image, self.rect)

    def ranDirection(self):
        num=random.randint(1,4)
        if num==1:
            return 'U'
        elif num==2:
            return 'R'
        elif num==3:
            return 'L'
        elif num==4:
            return 'D'
    # 战士随机移动的方法
    def randMove(self):
        if self.step<=0:
            self.direction=self.ranDirection()    # 修改方向
            self.step=120
        else:
            self.move()
            self.step-=1
    # 重新shot
    def shot(self):
        num=random.randint(1,100)
        if num<4:
            return Bullet(self)
# 子弹类
class Bullet(BaseItem):
    def __init__(self,play):
        self.image=pygame.image.load('bullet.png')
        self.direction=play.direction
        self.image=scaled_image4
        self.rect=self.image.get_rect()
        if self.direction=='U':
            self.rect.left=play.rect.left+play.rect.width/2-self.rect.width/2
            self.rect.top=play.rect.top-self.rect.height
        elif self.direction=='D':
            self.rect.left=play.rect.left+play.rect.width/2-self.rect.width/2
            self.rect.top=play.rect.top+play.rect.height
        elif self.direction=='L':
            self.rect.left=play.rect.left-self.rect.width/2-self.rect.width/2
            self.rect.top=play.rect.top+play.rect.width/2-self.rect.width/2
        elif self.direction=='R':
            self.rect.left=play.rect.left+play.rect.width
            self.rect.top=play.rect.top+play.rect.width/2-self.rect.width/2
        self.speed=6
        self.live=True
        self.attack=60        # 子弹攻击力

        # 显示
    def displayBullet(self):
        self.image = scaled_image4
        
        MainGame.window.blit(self.image,self.rect)
    # 移动
    def move(self):
        
        if self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
            else:
                self.live=False
        elif self.direction=='R':
            if self.rect.left+self.rect.width<SCREEN_WIDTH:
                self.rect.left+=self.speed
            else:
                self.live=False
        elif self.direction=='D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top+=self.speed
            else:
                self.live=False
        elif self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
            else:
                self.live=False

    def myBullt_hit_enemyplay(self):
        for enemyplay in MainGame.enemyplayList:
            if pygame.sprite.collide_rect(enemyplay,self):
                enemyplay.blood -= self.attack
                if enemyplay.blood <= 0:
                    enemyplay.live = False
                    explode=Explode(enemyplay)
                    MainGame.explodeList.append(explode)
                self.live=False
    def enemyBullet_hit_myplay(self):
        if MainGame.my_play and MainGame.my_play.live:
            if pygame.sprite.collide_rect(MainGame.my_play,self):
                MainGame.my_play.blood -= self.attack
                if MainGame.my_play.blood <= 0:
                    MainGame.my_play.live = False
                    explode=Explode(MainGame.my_play)
                    MainGame.explodeList.append(explode)
                self.live=False

# 爆炸类
class Explode:
    def __init__(self,play):
        self.rect=play.rect
        self.images=pygame.image.load('biast.png')
        self.live=True
    #显示爆炸
    def displayExplode(self):
        self.live=False
        MainGame.window.blit(self.images,self.rect)   
'''
# 音乐
class Music:
    def __init__(self):
        pass
    #播放音乐
    def play(self):
        pass
'''
if __name__ == '__main__':
    alit=int(input('欢迎来到‘反恐精英’，请玩家选择要使用的枪械:[0 AKM(7.62)]1 M416(5.56)][2 UMP-45(45口径)]'))
    qiang=['AKM(7.62)','M416(5.56)','UMP-45(45口径)']
    MainGame().startGame()