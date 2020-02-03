import example.cars
import example.engines

if __name__ == '__main__':
    gasoline_car = example.cars.Car(example.engines.GasolineEngine())
    diesel_car = example.cars.Car(example.engines.DieselEngine())
    electric_car = example.cars.Car(example.engines.ElectricEngine())

    print(gasoline_car)
