import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x % 60                                        # %: return the remainder of division
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")          # 02:  00:00:05 and not 00:00:5
    time.sleep(1)

print("TIME'S UP")