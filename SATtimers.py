import time
import winsound

#             reading,  writing,  math no calc. math calc 
timingArr = {"r": 780, "wr": 48, "mnc": 75, "mc":87}
count = 1
def timer(x):
    global count
    time.sleep(x)
    count += 1
    winsound.Beep(1000, 500)
    print("")
    print("*"*20)
    print("")
    print(f"should be on question {count}")
#reading, writing, math no calc, math calc 
# 0      , 1     , 2           , 3


inp = input("reading (r), writing (wri), math no calc (mnc), math calc (mc)")
rep = input("number of questions")

print(f"should be on question {count}")

for i in range(1, int(rep) + 1):
    timer(timingArr[inp])

