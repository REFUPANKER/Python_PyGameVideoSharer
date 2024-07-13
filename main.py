print("-------------------------------")
print("wellcome to pygame video sharer")

import gameVideoMaker as game,uploader

def Execute():
    game.Run()
    print("-------------------------------")
    uploader.Run()
    print("-------------------------------")

if __name__=="__main__":
    Execute()
    print("App ended")
    print("-------------------------------")