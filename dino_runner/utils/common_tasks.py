import pygame


'''
font = pygame.font.Font(FONT_STYLE, 22)
text = font.render("Press any key to start", True, (0, 0, 0))
text_rect = text.get_rect()
text_rect.center = (half_screen_width, half_screen_height)
self.screen.blit(text, text_rect)
'''

'''
https://pygame.readthedocs.io/en/latest/rect/rect.html
get_rect() possible values

x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h

'''

def textRender(fontStyle, fontSize, message, RGB = (0, 0, 0)):
    font = pygame.font.Font(fontStyle, fontSize)
    text = font.render(message, True, RGB)
    return text

def rectPosition(image, width, height, rectAlign = None):
    image_rect = image.get_rect()

    possiblePositionsX = ["left", "right", "centerx"]
    possiblePositionsY = ["top", "bottom", "centery"]
    possiblePositionsXY = [
        "topleft", "bottomleft", "topright", "bottomright",
        "midtop", "midleft", "midbottom", "midright",
        "center", ]

    if rectAlign.lower() in possiblePositionsX:
        setattr(image_rect, rectAlign.lower(), width)
    elif rectAlign.lower() in possiblePositionsY:
        setattr(image_rect, rectAlign.lower(), height)
    elif rectAlign.lower() in possiblePositionsXY:
        setattr(image_rect, rectAlign.lower(), (width, height))
    else:
        image_rect.x = width
        image_rect.y = height

    return image_rect