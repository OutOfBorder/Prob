import json
import cmath

def polar_to_complex(mag, angle_deg):
    return cmath.rect(mag, cmath.pi * angle_deg / 180)

def complex_to_polar(c):
    return abs(c), cmath.phase(c) * 180 / cmath.pi

def show(label, value):
    mag, ang = complex_to_polar(value)
    print(f"{label} = {mag:.3f} kA ∠ {ang:.2f}°")

# --- Загрузка токов из LabRZA ---
with open("lab_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

IA = polar_to_complex(*data["IA"])
IB = polar_to_complex(*data["IB"])
IC = polar_to_complex(*data["IC"])

print("📊 Токи из LabRZA (в кА):")
show("IA", IA)
show("IB", IB)
show("IC", IC)

# --- Расчёт тока КЗ вручную ---
U_phase = 220_000 / (3 ** 0.5)  # В
Z_total = complex(4.2701, 4.0)  # Ом

I_calc = U_phase / Z_total      # А
I_calc_ka = I_calc / 1000       # кА

print("\n📐 Расчётный ток КЗ вручную:")
show("I_calc", I_calc_ka)

# --- Функция сравнения ---
def compare(label, i_lab, i_calc):
    mag_lab, ang_lab = complex_to_polar(i_lab)
    mag_calc, ang_calc = complex_to_polar(i_calc)
    print(f"\n📉 Сравнение {label}:")
    print(f"  Модуль: Iab = {mag_lab:.3f} kA | Расчёт = {mag_calc:.3f} kA | Δ = {abs(mag_lab - mag_calc):.3f} kA")
    print(f"  Фаза:   Iab = {ang_lab:.2f}° | Расчёт = {ang_calc:.2f}° | Δ = {abs(ang_lab - ang_calc):.2f}°")

# --- Сравнение токов LabRZA с расчётным ---
compare("IA", IA, I_calc_ka)
compare("IB", IB, I_calc_ka)
compare("IC", IC, I_calc_ka)
