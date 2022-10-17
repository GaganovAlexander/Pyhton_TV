from TV import *

# Initialize module pygame, create mane surface: screen, make it full screen and fill white, then update
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
screen.fill(colors['white'])
pg.display.update()

# Create 10 class Channel objects, see module TV.py
Rosiya1 = Channel(r'TV_Records\Y2Mate.is - Жириновский обругал Собчак матом на дебатах. Собчак облила его водой-6rmP_S7QZho-720p-1655958971912.mp4',
                  r'TV_Records\[YT2mp3.info] - Жириновский обругал Собчак матом на дебатах. Собчак облила его водой (320kbps).mp3')
NTV_channel = Channel(r'TV_Records\[YT2mp3.info] - _Следствие вели_ Леонид Каневский - Уровень Плавных переходов.mp4', 
                      r'TV_Records\[YT2mp3.info] - __Следствие вели__ _ Леонид Каневский - Уровень Плавных переходов (320kbps).mp3')
STS = Channel(r'TV_Records\Кухня Сезон 4 Серия 7 (67).mp4', r'TV_Records\Кухня Сезон 4 Серия 7 (67).mp3')
Kvartal95 = Channel(r'TV_Records\[YT2mp3.info] - Рекорд по времени - за 5 минут на сцене Рассмеши комика выиграли 50000 гривен!.mp4', 
                    r'TV_Records\[YT2mp3.info] - Рекорд по времени - за 5 минут на сцене Рассмеши комика выиграли 50000 гривен! (192kbps).mp3')
Disney = Channel(r'TV_Records\финес и ферб 2 сезон 2 серия [TubeRipper.com].mp4',
                 r'TV_Records\[YT2mp3.info] - финес и ферб 2 сезон 2 серия (192kbps).mp3')
Nikelodeon = Channel(r'TV_Records\[YT2mp3.info] - Губка Боб Квадратные Штаны _ Просто любовь и никакого песка _ Nickelodeon Россия.mp4',
                     r'TV_Records\[YT2mp3.info] - Губка Боб Квадратные Штаны _ Просто любовь и никакого песка _ Nickelodeon Россия (192kbps).mp3')
TNT = Channel(r'TV_Records\Камеди Клаб Гость сорвал номер Иванов Смирнов Соболев Кравец Харламов [TubeRipper.com] (1).mp4',
              r'TV_Records\[YT2mp3.info] - Камеди Клаб «Гость сорвал номер» Иванов Смирнов Соболев Кравец Харламов (192kbps).mp3')
REN_TV = Channel(r'TV_Records\День военной тайны 26.09.2015 Фальсификация РЕН ТВ (отрывок) [TubeRipper.com].mp4',
                 r'TV_Records\[YT2mp3.info] - День военной тайны  26.09.2015 Фальсификация РЕН ТВ (отрывок) (192kbps).mp3')
Pyatnitsa = Channel(r'TV_Records\Орел и решка. Семья - Пятница [TubeRipper.com].mp4', r'TV_Records\[YT2mp3.info] - Орел и решка. Семья - Пятница (192kbps).mp3')
TNT4 = Channel(r'TV_Records\ПРЕМЬЕРА Прожарка на ТНТ4! [TubeRipper.com].mp4', r'TV_Records\[YT2mp3.info] - ПРЕМЬЕРА _ Прожарка на ТНТ4! (192kbps).mp3')
# Set them all into the tuple channels: first value of inner tuples is a Channel object, second - FPS of that Channel's video
channels = ((Rosiya1, 24), (NTV_channel, 25), (STS, 25), (Kvartal95, 25), (Disney, 24), (Nikelodeon, 25), (TNT, 25), (REN_TV, 25), (Pyatnitsa, 30), (TNT4, 25))

# Load and "draw" the TV as just a picture, scale it some biffer, set it pos from constants.py module
TV_sprite = pg.image.load(r'Sprites\TV1.png')
TV_sprite = pg.transform.scale(TV_sprite, (int(TV_sprite.get_width() * TV_RE_SCALE), int(TV_sprite.get_height() * TV_RE_SCALE)))
screen.blit(TV_sprite, (TV_POSX, TV_POSY))

# Doing the same thing with the Remote Controller, but without scaling
RC = pg.image.load(r'Sprites\4872.970.png')
screen.blit(RC, (RC_POSX, RC_POSY))

# Add some functioning buttons, just by create rectangles with size of the RC picture's buttons
# buttonOO - "button turn On/Off" is the red button on the RC wich will turn TV on/off
buttonOO = pg.Rect(RC_POSX + 20, RC_POSY + 20, 60, 40)
# buttons1_9_0 is a buttons from 1 to 9 + 0 on RC picture's buttons, they will change channels
buttons1_9_0 = []
for y in range(3):
    for x in range(3):
        buttons1_9_0.append(pg.Rect(RC_POSX + 25 + x*70, RC_POSY + 72 + y*63, 48, 45))
buttons1_9_0.append(pg.Rect(RC_POSX + 25 + 1*70, RC_POSY + 72 + 3*63, 48, 45))


clock = pg.time.Clock()     # Creating object clock to lock the FPS
run = True                  # run is a variable that make main cycle stoppable
i = 0                       # i variavle shows wich channel is now on
turn = False                # turn variable shows if the TV on or off(that need to the butoonOO)
while run:
    clock.tick(channels[i][1])      # Lock FPS with Channel's video FPS
    
    for event in pg.event.get():    # Looking for all events that happend that tick
        if event.type == pg.QUIT:   # if event is a window close - we are getting out of main cycle and end the script
            run = False


        if event.type == pg.KEYUP:          
            if event.key == pg.K_ESCAPE:        # if event is an escape keyup - doing same to the window close
                run = False


        if event.type == pg.MOUSEBUTTONDOWN:        # if event is mouse click, we will look for the place where that click was
            if buttonOO.collidepoint(event.pos):    # first - if the click was at buttonOO
                if not turn:                        # if TV is off we are turning it on and start playing the sound of video
                    turn = True                     # video will play by itself when turn is true, so we don't need to play it ourself
                    channels[i][0].sound.play()
                else:                               # if TV is already on - turning it off
                    turn = False                    # video will stop by itself
                    channels[i][0].sound.stop()     # stopping it's sound
                    channels[i][0].cap = cv2.VideoCapture(channels[i][0].video_path)    # recapture video because we need to play it from the beginning
                    pg.draw.rect(screen, colors['black'], (TV_POSX + 5, TV_POSY + 5, VID_WIDTH, VID_HEIGHT))    # drawing black screen on the TV's screen
                    
            for button in buttons1_9_0:     
                if button.collidepoint(event.pos) and turn:     # if click was at one of the buttons1_9_0 and tv is on
                    channels[i][0].sound.stop()     # we are stopping pevious channel sound
                    channels[i][0].cap = cv2.VideoCapture(channels[i][0].video_path)    # recapture it's video
                    i = buttons1_9_0.index(button)  # change the channel to the channel that user clicked
                    channels[i][0].sound.play()     # and play it's sound


    if turn:    # whenever the TV is on, we are playing video
        if channels[i][0].next_frame(screen):   # if there's some problem(or just video ended) - we just pass
            pass
            
    
    pg.display.flip()   # update display to the next frame(flip there just better then update, just trust me)

pg.quit()   # if main cycle is ended - we are ending the script