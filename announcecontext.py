class Announcecontext:
    def __enter__ (self):
        print("opened")
        return self
    
    def __exit__ (self, exc_val, exc_db, exc_type):
        print("closed")
        return False
    


with Announcecontext():
    print("Inside the widt-block")


#i didn't understand the concept but i was able to do it as this was from oops concept 