import os
import ctypes

# Commented code bellow detects screen resolutin
# on windows. Might be usful in near future

# Detect current resolution
user32 = ctypes.windll.user32
sysWidth = user32.GetSystemMetrics(0)
sysHeight = user32.GetSystemMetrics(1)

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
nextLevelKills = 15 # After how many kills should we raise the level

# Maximum bullets
gunMaxBullets = 10

# Stars
stars = []
starsLayer2 = []
maxStars = 200

# Initialized room
roomInit = False

# Step counter
steps = 0