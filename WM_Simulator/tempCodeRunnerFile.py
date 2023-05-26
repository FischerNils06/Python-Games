    running = True
    while running:
        for event in pygame.event.get():
            scoreboard()
            if event.type == pygame.QUIT:
                running = False

        scoreboard()