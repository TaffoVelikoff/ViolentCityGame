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
missed = 0