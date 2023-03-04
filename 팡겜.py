from cgitb import small
import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# 사라질 무기와 공 변수
weapon_to_remove = -1
ball_to_remove = -1

# fps
clock = pygame.time.Clock()

# os 쓰기위해 기본
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")

background = pygame.image.load(os.path.join(image_path,"640x480팡게임배경.jpeg"))

# 캐릭 and stage
stage = pygame.image.load(os.path.join(image_path,"stage.jpeg"))
stage_info = stage.get_rect().size
stage_width = stage_info[0]
stage_height = stage_info[1]
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

character =  pygame.image.load(os.path.join(image_path,"팡_캐릭.png"))
char_info = character.get_rect().size
char_width = char_info[0]
char_height = char_info[1]
char_x_pos = screen_width/2 - (char_width/2)
char_y_pos = screen_height - char_height - stage_height

# ball

balls = []
ball_images = [
    pygame.image.load(os.path.join(image_path,"공.jpeg")),
    pygame.image.load(os.path.join(image_path,"2번공.jpeg")),
    pygame.image.load(os.path.join(image_path,"3번공.jpeg")),
    pygame.image.load(os.path.join(image_path,"4번공.jpeg"))
    ]

ball_speed_y =[-18,-15,-12,-9]

# 최초 공 정의
balls.append({
    "ball_pos_x":50,
    "ball_pos_y":50,
    "ball_img_idx":0,
    "to_x":3,
    "to_y":6,
    "init_spd_y":ball_speed_y[0] 
})


# 왔다 갔다
char_to_x = 0

# 캐릭 속도

char_speed = 0.3 

# 무기

weapons = []

weapon = pygame.image.load(os.path.join(image_path,"무기.jpeg"))
weapon_info = weapon.get_rect().size
weapon_width = weapon_info[0]
weapon_height = weapon_info[1]
weapon_x_pos = 0
weapon_y_pos = screen_height - stage_height - char_height

# 무기 속도

weapon_speed = 0.1

running = True
while running == True:
    fps = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    char_to_x -= char_speed
                elif event.key == pygame.K_d:
                    char_to_x += char_speed
                elif event.key == pygame.K_SPACE:
                    weapon_x_pos = char_x_pos + (char_width/2) - (weapon_width/2)
                    weapons.append([weapon_x_pos,weapon_y_pos])
                    print(weapons)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                char_to_x = 0

    char_x_pos += char_to_x * fps

    weapons = [[w[0],w[1] - weapon_speed * fps] for w in weapons]
    
    weapons = [[w[0],w[1]] for w in weapons if w[1] >= 0]

    if char_x_pos >= screen_width - char_width:
        char_x_pos = screen_width - char_width
    elif char_x_pos <= 0:
        char_x_pos = 0

    # 공튕

    for idx, val in enumerate(balls):
        ball_pos_x = val["ball_pos_x"]
        ball_pos_y = val["ball_pos_y"]
        ball_img_idx = val["ball_img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x <= 0 or ball_pos_x >= screen_width-ball_width:
            val["to_x"] = val["to_x"] * -1

        if ball_pos_y >= screen_height - stage_height - ball_height:
            val["to_y"] = val["init_spd_y"]
        else:
            val["to_y"] += 0.5

        val["ball_pos_x"] += val["to_x"]
        val["ball_pos_y"] += val["to_y"]

    # 충돌 처리
    crash_char = character.get_rect()
    crash_char.left = char_x_pos
    crash_char.top = char_y_pos
    
    # 공과 캐릭터의 충돌
    for idx, val in enumerate(balls):
        ball_pos_x = val["ball_pos_x"]
        ball_pos_y = val["ball_pos_y"]
        ball_img_idx = val["ball_img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y


        if crash_char.colliderect(ball_rect):
            running = False
            break

        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = idx

                if ball_img_idx < 3 :
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    small_ball_rect = ball_images[ball_img_idx + 1 ].get_rect()
                    small_ball_width = small_ball_rect[0]
                    small_ball_height = small_ball_rect[1]

                    # 공 1
                    balls.append({
                        "ball_pos_x":ball_pos_x + (ball_width / 2) - ( small_ball_width/2),
                        "ball_pos_y":ball_pos_y+ (ball_height / 2) - ( small_ball_height/2),
                        "ball_img_idx":ball_img_idx + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_spd_y":ball_speed_y[ball_img_idx + 1] 
                    }
                    )
                    # 공 2
                    balls.append({
                        "ball_pos_x":ball_pos_x + (ball_width / 2) - ( small_ball_width/2),
                        "ball_pos_y":ball_pos_y+ (ball_height / 2) - ( small_ball_height/2),
                        "ball_img_idx":ball_img_idx + 1,
                        "to_x": +3,
                        "to_y": -6,
                        "init_spd_y":ball_speed_y[ball_img_idx + 1] 
                    }
                    )
                break
        else:
            continue    
        break
    
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    screen.blit(background,(0,0))
    
    for x_pos, y_pos in weapons:
        screen.blit(weapon,(x_pos,y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["ball_pos_x"]
        ball_pos_y = val["ball_pos_y"]
        print(ball_pos_x,ball_pos_y)
        ball_img_idx = val["ball_img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(stage,(stage_x_pos,stage_y_pos))
    screen.blit(character,(char_x_pos,char_y_pos))

    pygame.display.update()

pygame.quit()
