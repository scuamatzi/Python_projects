from rich.progress import track
import time

for i in track(range(10), description="Processing..."):
    #    print(f"working {i}")
    time.sleep(1)
