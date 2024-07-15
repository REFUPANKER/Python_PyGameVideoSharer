from datetime import datetime
import time,main
print("Infinite executer")
sleepTime=12*60*60
while True:
    print(">>> EXECUTED : "+str(datetime.now().strftime("%H:%M:%S")))
    main.Execute()
    print("-------------------------------")
    print(f"Next Execution in: {sleepTime // 3600} hour(s) {(sleepTime % 3600) // 60} minute(s) {sleepTime % 60} second(s)")
    time.sleep(sleepTime)  