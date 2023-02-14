# this is inheritance assigment

class Phone:
    def __init__(self, scty, network, dual, frontcamera, rearcamera, ram, storage):
        self.screentype = scty
        self.NetworkType = network
        if dual:
            self.dualsim = 1
        else:
            self.dualsim = 0
        if frontcamera == "5":
            self.frontcamera = "5"
        elif frontcamera == "8":
            self.frontcamera = "8"
        elif frontcamera == "12":
            self.frontcamera = "12"
        else:
            self.frontcamera = "16"
        if rearcamera == "8":
            self.rearcamera = "8"
        elif rearcamera == "12":
            self.rearcamera = "12"
        elif rearcamera == "16":
            self.rearcamera = "16"
        else:
            self.rearcamera = "32"
        if ram == "2":
            self.ram = "2"
        elif ram == "4":
            self.ram = "4"
        else:
            self.ram = "8"
        if storage == "16":
            self.storage = "16"
        elif storage == "32":
            self.storage = "32"
        else:
            self.storage = "64"

    def make_call(self):
        print("you can make call from it")

    def recieve_call(self):
        print("you can recieve call from it")

    def take_picture(self):
        print("you can take picture from it")


phone = Phone('touch', '4g', '1', '8', '12', '3', '16')
