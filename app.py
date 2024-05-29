#1. 量⼦化間隔
def qi_cv(Qi_a, Qi_b, Qi_n):
    return (Qi_b - Qi_a) / 2 ** Qi_n

#2. 代表値"
def tv_cv(Tv_a, Tv_b, Tv_n, Tv_k, Tv_w):
    if Tv_w == "Max":
        return Tv_a + Tv_k * ((Tv_b - Tv_a) / 2 ** Tv_n)
    elif Tv_w == "Min":
        return Tv_a + (Tv_k - 1) * ((Tv_b - Tv_a) / 2 ** Tv_n)
    elif Tv_w == "Med":
        return Tv_a + (Tv_k - 0.5) * ((Tv_b - Tv_a) / 2 ** Tv_n)
    else:
        return "Error"

#3. 二進数表示
def calculate_quantization_interval(x, y, n):
    return (y - x) / (2 ** n)

def ad_conversion_result(x, y, n, value):
    q_interval = calculate_quantization_interval(x, y, n)
    m = int((value - x) / q_interval)
    binary_result = bin(m)
    return binary_result[2:].zfill(int(n)) 

#4. 量子化誤差1（量子化誤差の最大値）
def qe1_cv(Qe1_a, Qe1_b, Qe1_n, Qe1_w):
    if Qe1_w == "Max" or Qe1_w == "Min":
        return (Qe1_b - Qe1_a) / 2 ** Qe1_n
    elif Qe1_w == "Med":
        return ((Qe1_b - Qe1_a) / 2 ** Qe1_n) / 2
    else:
        return "Error"

#5. 量子化誤差2（kに対する量子化誤差）
def qe2_cv(Qe2_a, Qe2_b, Qe2_n, Qe2_k, Qe2_w):
    dis = (Qe2_b - Qe2_a) / 2 ** Qe2_n
    tmp = 0

    interval_index = int((Qe2_k - Qe2_a) / dis)
    interval_start = Qe2_a + interval_index * dis
    interval_end = interval_start + dis

    while tmp < Qe2_k:
        tmp += dis
    if Qe2_w == "Max":
        return tmp - Qe2_k
    elif Qe2_w == "Min":
        representative_value = interval_start
        quantization_error = abs(Qe2_k - representative_value)
        return quantization_error
    elif Qe2_w == "Med":
        median = (interval_start + interval_end) / 2
        quantization_error = abs(Qe2_k - median)
        return quantization_error
    else:
        return "Error"
    
#6. A/D-D/A 変換
def ada_cv(Ada_a, Ada_b, Ada_n, Ada_k, Ada_w):
    dis = (Ada_b - Ada_a) / 2 ** Ada_n
    tmp = 0
    while tmp < Ada_k:
        tmp += dis
    if Ada_w == "Max":
        return tmp
    elif Ada_w == "Min":
        return tmp - dis
    elif Ada_w == "Med":
        return (tmp + (tmp - dis)) / 2
    else:
        return "Error"

def main():
    while True:
        print("計算システムを選択してください:")
        print("1. 量⼦化間隔")
        print("2. 代表値")
        print("3. 二進数表示 or kに対する区間番号(出力値+1が答え)")
        print("4. 量子化誤差1（量子化誤差の最大値）")
        print("5. 量子化誤差2（kに対する量子化誤差）")
        print("6. A/D-D/A 変換")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            Qi_a = float(input("Enter a: "))
            Qi_b = float(input("Enter b: "))
            Qi_n = float(input("Enter n: "))
            print("Result:", qi_cv(Qi_a, Qi_b, Qi_n))

        elif choice == '2':
            Tv_a = float(input("Enter a: "))
            Tv_b = float(input("Enter b: "))
            Tv_n = float(input("Enter n: "))
            Tv_k = float(input("Enter k: "))
            Tv_w = input("Enter (Max/Min/Med): ")
            print("Result:", tv_cv(Tv_a, Tv_b, Tv_n, Tv_k, Tv_w))

        elif choice == '3':
            Tv_a = float(input("Enter a: "))
            Tv_b = float(input("Enter b: "))
            Tv_n = float(input("Enter n: "))
            Tv_k = float(input("Enter k: "))
            print("Result:", ad_conversion_result(Tv_a, Tv_b, Tv_n, Tv_k))

        elif choice == '4':
            Qe1_a = float(input("Enter a: "))
            Qe1_b = float(input("Enter b: "))
            Qe1_n = float(input("Enter n: "))
            Qe1_w = input("Enter (Max/Min/Med): ")
            print("Result:", qe1_cv(Qe1_a, Qe1_b, Qe1_n, Qe1_w))

        elif choice == '5':
            Qe2_a = float(input("Enter a: "))
            Qe2_b = float(input("Enter b: "))
            Qe2_n = float(input("Enter n: "))
            Qe2_k = float(input("Enter k: "))
            Qe2_w = input("Enter (Max/Min/Med): ")
            print("Result:", qe2_cv(Qe2_a, Qe2_b, Qe2_n, Qe2_k, Qe2_w))

        elif choice == '6':
            Ada_a = float(input("Enter a: "))
            Ada_b = float(input("Enter b: "))
            Ada_n = float(input("Enter n: "))
            Ada_k = float(input("Enter k: "))
            Ada_w = input("Enter (Max/Min/Med): ")
            print("Result:", ada_cv(Ada_a, Ada_b, Ada_n, Ada_k, Ada_w))

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()