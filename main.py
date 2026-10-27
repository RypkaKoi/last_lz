from pyramid import volume
from archimed import is_floating

def main():
    S1 = float(input("Введите площадь верхнего основания: "))
    S2 = float(input("Введите площадь нижнего основания: "))
    h = float(input("Ввеедите высоту: "))
    
    V = volume(S1, S2, h)
    print(f"Объем усеченной пирамиды: {V:.2f}")

    m = float(input("Введите массу предмета кг: "))
    Vol = float(input("Введите объеем погруженной части м³: "))
    Dens = float(input("Введите плотность премдета кг/м³: "))

    if (is_floating(m , Vol , Dens)):
        print("Плывет")
    else: 
        print("Не плывет")

if __name__ == "__main__":
    main()