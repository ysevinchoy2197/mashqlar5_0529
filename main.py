class Manzil:
    def __init__(self, shahar):
        self.shahar = shahar

    def show_manzil(self):
        print("Shahar:", self.shahar)


class Shaxs:
    def __init__(self, ism, shahar):
        self.ism = ism
        self.manzil = Manzil(shahar)

    def show_shaxs(self):
        print("Ism:", self.ism)
        print("Shahar:", self.manzil.shahar)


s = Shaxs("Dilnoza", "Samarqand")

s.show_shaxs()
