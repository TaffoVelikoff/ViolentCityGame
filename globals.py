import os

# Define dirs
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

# Default screen width / height
winWidth = 1366
winHeight = 768

# Score & stats
kills = 0
score = 0
shots = 0
scorePerKill = 2 # How many points per kill per level

# Missed
missed = 0
maxMissed = 20 

# Enemy speed
level = 1 # Enemy speed = starting speed + level
nextLevelKills = 10 # After how many kills should we raise the level

gunMaxBullets = 10

roomInit = False