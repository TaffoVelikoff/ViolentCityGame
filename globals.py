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

# Debug Mode
debug = False

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

# Draw killed enemy score
enemyScore = [0, 0, 0, 0]
enemyScorePos = 0
enemyScorePosChange = False

# Timers
timerPowerUp = 30 # How many seconds to create a new power up
timerPowerUpDestroy = 3 # How many seconds a power up stays on screen

# Maximum bullets
gunMaxBullets = 10

# Stars
stars = []
starsLayer2 = []
maxStars = 200

# This will help us draw a text when 
# a power-up has been collected
powerText = ''
drawPowerText = False
drawPowerTextStart = 0

# Power-ups
pwrBulletsAmount = 10 # How many bullets should be added for the BulletPlus()

# Initialized room
roomInit = False

# Fremes per second
FPS = 60

# Minute (how many steps in minute)
minute = FPS*60

# Seconds (how many steps in second)
# It's the FPS, but a var "second" makes the code
# more readible...
second = FPS

# Step counter
steps = 0