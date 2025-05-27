class engine:
    def turnon(self):
        print("The engine has turned on")

    def turnoff(self):
        print("The kill switch has been pressed, Engine off.")

class remote:
    def __init__(self):
        self.engine = engine()

    def turnon(self):
        self.engine.turnon()

    def turnoff(self):
        self.engine.turnoff()
remote = remote()
remote.turnon()
remote.turnoff()
