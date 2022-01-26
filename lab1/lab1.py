class Computer:
    def __init__(self, cpu, mainboard, ram_gb, psu, ssd_gb):
        self.cpu = cpu
        self.mainboard = mainboard
        self.ram = ram_gb
        self.psu = psu
        self.ssd = ssd_gb

class Customer:
    def __init__(self, name, age, address, computer_qty):
        self.name = name
        self.age = age
        self.address = address
        self.computer_qty = computer_qty

class Laptop:
    def __init__(self, cpu, ram, gpu, brand):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.brand = brand


com1 = Computer('i3', 'h410', 4, '350watt', 120)
com2 = Computer('i5', 'b460', 8, '550watt', 240)
com3 = Computer('i7', 'z490', 16, '650watt', 512)

com1.ssd += 120


print((com1.cpu), (com1.mainboard), (com1.ram), (com1.psu), (com1.ssd))
print((com2.cpu), (com2.mainboard), (com2.ram), (com2.psu), (com2.ssd))
print((com3.cpu), (com3.mainboard), (com3.ram), (com3.psu), (com3.ssd))

cus1 = Customer('Atakorn', 20, 'Minburi', 2)
cus2 = Customer('Sanya', 20, 'Nongchok', 5)
cus3 = Customer('Athiwat', 21, 'Ladkrabang', 4)

cus1.computer_qty += 1


print((cus1.name), (cus1.age), (cus1.address), (cus1.computer_qty))
print((cus3.name), (cus3.age), (cus3.address), (cus3.computer_qty))


lap1 = Laptop('Ryzen3', 4, 'radeon graphic', 'HP')
lap2 = Laptop('Ryzen5', 8, 'gtx1650', 'ASUS')
lap3 = Laptop('Ryzen7', 16, 'rtx3070', 'MSI')

print((lap1.cpu), (lap1.cpu), (lap1.ram), (lap1.gpu), (lap1.brand))
print((lap2.cpu), (lap2.cpu), (lap2.ram), (lap2.gpu), (lap2.brand))







        
        