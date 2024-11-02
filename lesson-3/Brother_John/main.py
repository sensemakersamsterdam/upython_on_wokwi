from time import sleep
import picozero as pz

sp = pz.Speaker(26)

sp.play(n=None, wait=False, volume = 0.1, tune=
    # Are you sleeping, * 2
    (
        ('g4', 0.3),
        ('a4', 0.3),
        ('b4', 0.35),
        ('g4', 0.3),
        (None, 0.05)
    ) * 2 + 
    # Brother John, * 2
    (
        ('b4', 0.3),
        ('c5', 0.3),
        ('d5', 0.3),
        (None, 0.2)
    ) * 2 + 
    # Morning bells are ringing, *2
    (
        ('d5', 0.3),
        ('e5', 0.25),
        ('d5', 0.3),
        ('c5', 0.3),
        ('b4', 0.35),
        ('g4', 0.35),
        (None, 0.3)
    ) * 2 +
    # Ding, dang, dong,
    (
        ('g4', 0.3),
        ('d4', 0.3),
        ('g4', 0.4),
        (None, 0.2)
    ) * 2 +
    (None, 1) 
)
