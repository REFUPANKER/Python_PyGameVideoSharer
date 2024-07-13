from datetime import datetime
import time,index
print("Infinite executer")
stack=0
sleepTime=5*60
while stack<5:
    stack+=1
    print(">>> EXECUTED : "+str(datetime.now().strftime("%H:%M:%S")))
    index.Execute()
    print("-------------------------------")
    print(f"Next Execution in: {sleepTime // 3600} hour(s) {(sleepTime % 3600) // 60} minute(s) {sleepTime % 60} second(s)")
    time.sleep(sleepTime)  