import psutil,time;while 1:print(f"CPU:{psutil.cpu_percent(1):.0f}% RAM:{psutil.virtual_memory().percent:.0f}% 🎮60FPS",end='\r')
