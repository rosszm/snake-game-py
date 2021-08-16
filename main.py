# Snake V 1.0

# main.py()
# contains the setup and event loop; runs the program Snake

# Created By: Zack Ross
# Last Updated: May 6, 2017


import pygame
from pygame.locals import *
import snake as s
import wall as w
import food as f
import file_helper as fh
import os


def main():
    """
    Runs the program.

    :return: None
    """
    # Load high score
    if not os.path.isfile("highscore.txt"):
        fh.write_file("highscore.txt", [0])
    high_score = fh.read_file("highscore.txt")[0]

    # Setup window
    pygame.init()

    window_x = 630
    window_y = 690

    screen = pygame.display.set_mode((window_x, window_y), HWSURFACE | DOUBLEBUF)
    pygame.display.set_caption('Snake')

    pygame.mouse.set_visible(False)

    border = pygame.Surface(screen.get_size())
    border.fill((250, 150, 100))
    border_pos = (0, 0)
    background = pygame.Surface((600, 600))

    clock = pygame.time.Clock()
    fps = 12

    # Setup texts
    title_font = pygame.font.SysFont("Fipps Regular", 38)
    game_over_font = pygame.font.SysFont("Fipps Regular", 30)
    default_font = pygame.font.SysFont("Fipps Regular", 16)
    small_font = pygame.font.SysFont("Fipps Regular", 12)

    title = title_font.render("SNAKE", 1, (0, 0, 0))
    title_pos = (15, -10)

    score_label = default_font.render("SCORE :", 1, (0, 0, 0))
    score_label_pos = (350, 31)
    score_pos = (score_label_pos[0] + score_label.get_width() + 15, score_label_pos[1])

    high_score_label = default_font.render("HIGH SCORE :", 1, (0, 0, 0))
    high_score_label_pos = (350, 0)

    high_score_text = default_font.render(high_score, 1, (0, 0, 0))
    high_score_text_pos = (high_score_label_pos[0] + high_score_label.get_width() + 15, high_score_label_pos[1])

    game_over_border = pygame.Surface([300, 165])
    game_over_border.fill((250, 250, 250))
    game_over_border_pos = (window_x // 2 - (game_over_border.get_width() // 2),
                            window_y // 2 - (game_over_border.get_height() // 2))

    game_over_box = pygame.Surface([game_over_border.get_width() - 8, game_over_border.get_height() - 8])
    game_over_box.fill((0, 0, 0))
    game_over_box_pos = (window_x // 2 - (game_over_box.get_width() // 2), game_over_border_pos[1] + 4)

    game_over_label = game_over_font.render("GAME OVER!", 1, (250, 250, 250))
    game_over_label_pos = (window_x // 2 - (game_over_label.get_width() // 2), game_over_box_pos[1])

    message = "YOUR SCORE IS 1"
    message_label = small_font.render(message, 1, (250, 250, 250))
    message_label_pos = (window_x // 2 - (message_label.get_width() // 2), game_over_label_pos[1] + 60)

    new_high_score_label = small_font.render("** NEW HIGH SCORE **", 1, (250, 250, 250))
    new_high_score_label_pos = (window_x // 2 - (new_high_score_label.get_width() // 2), message_label_pos[1] + 30)

    restart_label = small_font.render('PRESS "SPACE" TO RESTART', 1, (250, 250, 250))
    restart_label_pos = (window_x // 2 - (restart_label.get_width() // 2), new_high_score_label_pos[1] + 30)

    # Create snake sprite
    snake_start_pos = 15, 75
    snake_speed = 15

    snake_group = pygame.sprite.Group()
    snake = s.Snake(snake_start_pos[0], snake_start_pos[1])
    snake_group.add(snake)

    # Create wall sprites
    wall_group = pygame.sprite.Group()

    wall_pos_list = [(0, 75), (615, 75), (15, 60), (15, 675)]
    wall_rect_list = [(15, 600), (15, 600), (600, 15), (600, 15)]
    for i in range(4):
        wall = w.Wall(wall_pos_list[i], wall_rect_list[i])
        wall_group.add(wall)

    # Create food sprite
    food_group = pygame.sprite.GroupSingle()
    food = f.Food()
    food_group.add(food)

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    snake.direction(snake_speed, 0)

                elif event.key == K_LEFT:
                    snake.direction(-snake_speed, 0)

                elif event.key == K_DOWN:
                    snake.direction(0, snake_speed)

                elif event.key == K_UP:
                    snake.direction(0, -snake_speed)

                if event.key == K_SPACE:
                    snake.reset(snake_start_pos[0], snake_start_pos[1])
                    food_group.add(f.Food())

        new_high_score = snake.length > int(high_score)

        # Check if game is over
        if len(pygame.sprite.spritecollide(snake, wall_group, False, False)) > 0 or snake.collide_self():
            snake.direction(0, 0)
            screen.blit(game_over_border, game_over_border_pos)
            screen.blit(game_over_box, game_over_box_pos)

            if new_high_score:
                fh.write_file("highscore.txt", [str(snake.length)])
                screen.blit(new_high_score_label, new_high_score_label_pos)

            message = "YOUR SCORE IS  " + str(snake.length)
            message_label = small_font.render(message, 1, (250, 250, 250))
            message_label_pos = (window_x // 2 - (message_label.get_width() // 2), game_over_label_pos[1] + 60)

            screen.blit(game_over_label, game_over_label_pos)
            screen.blit(message_label, message_label_pos)
            screen.blit(restart_label, restart_label_pos)
        else:
            # Check if the snake has reached the food
            if len(pygame.sprite.spritecollide(snake, food_group, False, False)) > 0:
                food = f.Food()
                food_group.add(food)
                snake.grow()

            # Update and refresh screen
            screen.blit(border, border_pos)
            screen.blit(title, title_pos)

            screen.blit(score_label, score_label_pos)
            screen.blit(high_score_label, high_score_label_pos)

            score = default_font.render(str(snake.length), 1, (0, 0, 0))
            screen.blit(score, score_pos)
            screen.blit(high_score_text, high_score_text_pos)

            if new_high_score:
                high_score_text = default_font.render(str(snake.length), 1, (0, 0, 0))

            screen.blit(background, snake_start_pos)

            food_group.draw(screen)

            snake.update()
            snake.show(screen)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()
