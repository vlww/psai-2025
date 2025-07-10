import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trainervrse - Shooting Drill")

# Load images
background_img = pygame.image.load("project/background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

goal_img = pygame.image.load("project/goal.png")
goal_img = pygame.transform.scale(goal_img, (WIDTH, 300))

ball_img = pygame.image.load("project/soccer_ball.png")
ball_img = pygame.transform.scale(ball_img, (50, 50))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 100, 0)

# Fonts
font = pygame.font.SysFont(None, 36)

# Game variables
target_width = 100
target_height = 50
target_x = random.randint(100, WIDTH - 200)
target_y = random.randint(100, 120)
score = 0
shots = 0
difficulty = 1
success_rate = []

# Ball position
ball_x = WIDTH // 2 - 25
ball_y = HEIGHT - 100
kick_in_progress = False
kick_target = (0, 0)

clock = pygame.time.Clock()

def show_text(text, x, y):
    label = font.render(text, True, BLUE)
    screen.blit(label, (x, y))

def adjust_difficulty():
    global target_width, difficulty
    if len(success_rate) >= 5:
        recent = success_rate[-5:]
        avg = sum(recent) / 5
        if avg > 0.8 and difficulty < 5:
            difficulty += 1
        elif avg < 0.4 and difficulty > 1:
            difficulty -= 1

        target_width = max(50, 100 - (difficulty - 1) * 10)

def animate_kick():
    global kick_in_progress, ball_x, ball_y
    dx = (kick_target[0] - ball_x) / 10
    dy = (kick_target[1] - ball_y) / 10
    ball_x += dx
    ball_y += dy
    if abs(ball_x - kick_target[0]) < 10 and abs(ball_y - kick_target[1]) < 10:
        check_goal()
        reset_kick()

def check_goal():
    global score, shots, success_rate
    shots += 1
    if target_x <= kick_target[0] <= target_x + target_width and target_y <= kick_target[1] <= target_y + target_height:
        score += 1
        success_rate.append(1)
    else:
        success_rate.append(0)
    adjust_difficulty()

def reset_kick():
    global kick_in_progress, ball_x, ball_y, target_x, target_y
    kick_in_progress = False
    ball_x = WIDTH // 2 - 25
    ball_y = HEIGHT - 100
    target_x = random.randint(100, WIDTH - 200)
    target_y = random.randint(100, 120)


def draw_transparent_target(x, y, w, h, alpha=128):
    target_surface = pygame.Surface((w, h), pygame.SRCALPHA)
    target_surface.fill((100, 0, 0, alpha))  # Dark green with transparency
    screen.blit(target_surface, (x, y))

# Main loop
running = True
while running:
    screen.blit(background_img, (0, 0))
    screen.blit(goal_img, (0, 0))

    # Draw target area
    draw_transparent_target(target_x, target_y, target_width, target_height)

    # Draw ball
    screen.blit(ball_img, (ball_x, ball_y))

    # Animate ball
    if kick_in_progress:
        animate_kick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not kick_in_progress:
            kick_target = pygame.mouse.get_pos()
            kick_in_progress = True

    # Display stats
    show_text(f"Score: {score}/{shots}", 10, 10)
    show_text(f"Difficulty: {difficulty}", 10, 50)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
