volume = lambda S1, S2, h: (h / 3) * (S1 + S2 + (S1 * S2) ** 0.5)

if __name__ == "__main__":
    S1 = float(input("Введите площадь верхнего основания: "))
    S2 = float(input("Введите площадь нижнего основания: "))
    h = float(input("Введите высоту: "))
    
    V = volume(S1, S2, h)
    print(f"Объем усеченной пирамиды: {V:.2f}")