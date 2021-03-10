import os,time,datetime,asyncio,winsound
from tim_var import*

os.system('title TIMERNATOR')

while True:
    for x in range(4):
        os.system(special_fx[2])
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )
        
        exec(redundant_code1)
        
        for y in range(4):
            timer=datetime.datetime.now()
            exec(redundant_code2)
            
        time.sleep(1)
        
        os.system(special_fx[2])
        
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )
        
        exec(redundant_code1)
        
        for y in range(4):
            timer=datetime.datetime.now()
            exec(redundant_code2)
            
        time.sleep(1)
        
        os.system(special_fx[2])
        
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )
        
        exec(redundant_code1)
        
        for y in range(4):
            timer=datetime.datetime.now()
            exec(redundant_code2)
            
        time.sleep(1)
