import time
from plyer import notification

while True:
    print("Drink some water")
    notification.notify(title = "Drink some water" , message = "Drink water reminder")

    
    
    time.sleep(60*60)