import cmath

# Входные параметры
U_phase = 220 / (3 ** 0.5)  # фазное напряжение, В
Z_source = complex(0.5, 0.2)  # Ом
Z_line = complex(0.8, 0.4)    # Ом
Z_total = Z_source + Z_line

# Расчёт тока КЗ
I_fault = U_phase / Z_total

# Вывод результата
print(f"Ток КЗ (модуль): {abs(I_fault):.2f} А")
print(f"Ток КЗ (фаза): {cmath.phase(I_fault) * 180 / cmath.pi:.2f}°")