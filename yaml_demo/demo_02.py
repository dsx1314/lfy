import sys
import random
import pygame
from pygame.locals import *

width, height = 640, 480
background = (0, 191, 255)


# 按钮
def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.font('./font/simkai.ttf', 20)
    textrender = font.render(text, True, (0, 0, 0))
    textrect = textrender.get_rect()
    textrect.center = ((x + w / 2), (y + h / 2))
    screen.blit(textrender, textrect)


# 标题
def title(text, screen, scale, color=(255, 0, 0)):
    font = pygame.font.font('./font/simkai.ttf', width // (len(text) * 2))
    textrender = font.render(text, True, color)
    textrect = textrender.get_rect()
    textrect.midtop = (width / scale[0], height / scale[1])
    screen.blit(textrender, textrect)


# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, 620), random.randint(20, 460)
    return x, y


# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
    screen.fill(background)
    font = pygame.font.font('./font/simkai.ttf', width // (len(text)))
    textrender = font.render(text, True, color)
    textrect = textrender.get_rect()
    textrect.midtop = (width / 2, height / 2)
    screen.blit(textrender, textrect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == quit:
                pygame.quit()
            sys.exit()

# 主函数
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption('from一个喜欢你很久的小哥哥')
    clock = pygame.time.Clock()
    pygame.mixer.music.load('./BEYOND - 谁伴我闯荡.mp3')
    pygame.mixer.music.play(-1, 30.0)
    pygame.mixer.music.set_volume(0.25)
    unlike_pos_x = 330
    unlike_pos_y = 300
    unlike_pos_width = 100
    unlike_pos_height = 50
    like_pos_x = 180
    like_pos_y = 300
    like_pos_width = 100
    like_pos_height = 50
    running = True
    like_color = (255, 0, 255)
    while running:
        screen.fill(background)
    img = pygame.image.load("./1653015757(1).jpg")
    imgrect = img.get_rect()
    imgrect.midtop = width // 2, height // 4
    screen.blit(img, imgrect)
    for event in pygame.event.get():
        if event.type == pygame.mousebuttondown:
            mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < like_pos_x + like_pos_width + 5 and mouse_pos[0] > like_pos_x - 5 and \
                mouse_pos[1] < like_pos_y + like_pos_height + 5 and mouse_pos[1] > like_pos_y - 5:
            like_color = background
            running = False
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] < unlike_pos_x + unlike_pos_width + 5 and mouse_pos[0] > unlike_pos_x - 5 and \
            mouse_pos[1] < unlike_pos_y + unlike_pos_height + 5 and mouse_pos[1] > unlike_pos_y - 5:
        while True:
            unlike_pos_x, unlike_pos_y = get_random_pos()
            if mouse_pos[0] < unlike_pos_x + unlike_pos_width + 5 and mouse_pos[0] > unlike_pos_x - 5 and \
                mouse_pos[1] < unlike_pos_y + unlike_pos_height + 5 and mouse_pos[1] > unlike_pos_y - 5:
                continue
            break
    title('小姐姐，我观察你很久了', screen, scale=[2, 10])
    title('做我女朋友好不好呀', screen, scale=[2, 6])
    button('好呀', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
    button('算了吧', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, (255, 0, 255), screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
    show_like_interface('我就知道小姐姐你也喜欢我~', screen, color=(255, 0, 0))


if __name__ == '__main__':
    main()