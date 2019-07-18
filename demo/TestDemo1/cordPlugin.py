class cordPlugin:
    def __init__(self,name):
        self.name = name

    def test(self):
        print("我是%s" % self.name)