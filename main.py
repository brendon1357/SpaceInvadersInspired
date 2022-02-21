import pygame
import random
import math
from sys import exit


def intro_screen():
    pygame.init()

    font = pygame.font.SysFont("arial", 30)

    header_font = pygame.font.SysFont("arial", 46)

    topIcon = pygame.image.load("Images/space-ship.png")

    pygame.display.set_icon(topIcon)

    pygame.display.set_caption("Space Invaders Remake")

    intro_message = header_font.render("Space Invaders Remake", True, (0, 255, 0))
    intro_message_2 = font.render("Spacebar - Start game", True, (255, 255, 255))
    intro_message_3 = font.render("ESC - Exit game", True, (255, 255, 255))
    intro_message_4 = font.render("R - Restart game/return to main menu", True, (255, 255, 255))

    windowScreen = pygame.display.set_mode((800, 600))

    intro = True

    while intro:

        windowScreen.fill((0, 0, 0))

        windowScreen.blit(intro_message, [800/2 - intro_message.get_width()/2, 200/2 - intro_message.get_height()/2])
        windowScreen.blit(intro_message_2, [800/2 - intro_message_2.get_width()/2, 400/2 - intro_message_2.get_height()/2])
        windowScreen.blit(intro_message_3, [800/2 - intro_message_3.get_width()/2, 600/2 - intro_message_3.get_height()/2])
        windowScreen.blit(intro_message_4, [800/2 - intro_message_4.get_width()/2, 800/2 - intro_message_4.get_height()/2])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    intro = False
                    exit()

        pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()

    backgroundImg = pygame.image.load("Images/Spacepic.jpg")

    windowScreen = pygame.display.set_mode((800, 600))

    score_num = 0
    font = pygame.font.SysFont("arial", 30)

    topIcon = pygame.image.load("Images/space-ship.png")

    pygame.display.set_icon(topIcon)

    pygame.display.set_caption("Space Invaders Remake")

    playerImg = pygame.image.load("Images/space-invaders.png")
    playerX = 370
    playerY = 480
    playerX_change = 0

    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 12
    initial_num_of_enemies = 6

    bulletImg = pygame.image.load("Images/bullet.png")
    bulletX = 0
    bulletY = 480
    bulletY_change = 35
    bullet_state = "ready"

    lives = 3
    end_lives = 0

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load("Images/ufo.png"))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(0, 0))
        enemyX_change.append(8)
        enemyY_change.append(40)
        num_of_enemies = initial_num_of_enemies


    def isCollision():
        distance = math.sqrt((math.pow(enemyX[i] - bulletX, 2)) + (math.pow(enemyY[i] - bulletY, 2)))
        if distance < 28:
            return True
        else:
            return False


    def show_score():
        score = font.render("Score: " + str(score_num), True, (0, 255, 0))
        windowScreen.blit(score, [800/2 - score.get_width()/2, 5])


    def show_score_to_win():
        win_score = font.render("Score to win: 100", True, (255, 255, 255))
        windowScreen.blit(win_score, (10, 5))


    def you_win_msg():
        win_text = font.render("You win, CONGRATULATIONS!", True, (255, 255, 255))
        windowScreen.blit(win_text, [800/2 - win_text.get_width()/2, 200 - win_text.get_height()/2])

        if lives == 1:
            show_lives_left = font.render("You had " + str(lives) + " life left", True, (255, 255, 255))
            windowScreen.blit(show_lives_left,
                              [800/2 - show_lives_left.get_width()/2, 275 - show_lives_left.get_height()/2])
        elif lives == 2 or 3:
            show_lives_left = font.render("You had " + str(lives) + " lives left", True, (255, 255, 255))
            windowScreen.blit(show_lives_left, [800/2 - show_lives_left.get_width()/2, 275 - show_lives_left.get_height()/2])

        return_text = font.render("Press R to return to the main menu", True, (255, 255, 255))
        windowScreen.blit(return_text, [800/2 - return_text.get_width()/2, 350 - return_text.get_height()/2])


    def game_over():
        lose_text = font.render("You lose, GAME OVER!", True, (255, 255, 255))
        windowScreen.blit(lose_text, [800/2 - lose_text.get_width()/2, 400/2 - lose_text.get_height()/2])
        return_text = font.render("Press R to return to the main menu", True, (255, 255, 255))
        windowScreen.blit(return_text, [800 / 2 - return_text.get_width() / 2, 600 / 2 - return_text.get_height() / 2])


    def player():
        windowScreen.blit(playerImg, (playerX, playerY))


    def enemy(x, y, i):
        windowScreen.blit(enemyImg[i], (x, y))


    def show_lives():
        lives_display = font.render("Lives: " + str(lives), True, (255, 255, 255))
        windowScreen.blit(lives_display, (10, 35))


    def draw_line():
        color_line = (255, 0, 0)
        pygame.draw.line(windowScreen, color_line, (0, 445), (800, 445))


    rungame = True

    while rungame:
        windowScreen.fill((0, 0, 0))
        windowScreen.blit(backgroundImg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rungame = False
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -10

                elif event.key == pygame.K_RIGHT:
                    playerX_change = 10

                elif event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletX = playerX
                        bullet_state = "fire"
                        windowScreen.blit(bulletImg, (bulletX + 15, bulletY))

                elif event.key == pygame.K_ESCAPE:
                    rungame = False
                    exit()
                elif event.key == pygame.K_r:
                    intro_screen()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if playerX_change < 0:
                        playerX_change = 0

                elif event.key == pygame.K_RIGHT:
                    if playerX_change > 0:
                        playerX_change = 0

        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
            
        if playerX >= 736:
            playerX = 736

        for i in range(num_of_enemies):
            enemy(enemyX[i], enemyY[i], i)
            enemyX[i] += enemyX_change[i]

            if 0 <= score_num < 20:
                if enemyX[i] <= 0:
                    enemyX_change[i] = 10
                    enemyY[i] += enemyY_change[i]

                elif enemyX[i] >= 736:
                    enemyX_change[i] = -10
                    enemyY[i] += enemyY_change[i]

            elif 20 <= score_num < 40:
                if enemyX[i] <= 0:
                    enemyX_change[i] = 11
                    enemyY[i] += enemyY_change[i]

                elif enemyX[i] >= 736:
                    enemyX_change[i] = -11
                    enemyY[i] += enemyY_change[i]

            elif 40 <= score_num < 80:
                if enemyX[i] <= 0:
                    enemyX_change[i] = 11.5
                    enemyY[i] += enemyY_change[i]

                elif enemyX[i] >= 736:
                    enemyX_change[i] = -11.5
                    enemyY[i] += enemyY_change[i]

            elif 80 <= score_num < 100:
                if enemyX[i] <= 0:
                    enemyX_change[i] = 12.25
                    enemyY[i] += enemyY_change[i]

                elif enemyX[i] >= 736:
                    enemyX_change[i] = -12.25
                    enemyY[i] += enemyY_change[i]

            collision = isCollision()
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_num += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 0)

            elif score_num == 100:
                for j in range(num_of_enemies):
                    enemyY[j] = 1000
                you_win_msg()
                break

            if lives >= end_lives:
                if 435 < enemyY[i] < 900:
                    enemyY[i] = 1000
                    lives -= 1

                    if score_num > 0:
                        score_num -= 1

            elif lives == end_lives:
                for j in range(num_of_enemies):
                    enemyY[j] = 1000
                game_over()
                break

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            bullet_state = "fire"
            windowScreen.blit(bulletImg, (bulletX + 15, bulletY))
            bulletY -= bulletY_change

        draw_line()
        player()
        show_score()
        show_score_to_win()
        show_lives()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
	intro_screen()
