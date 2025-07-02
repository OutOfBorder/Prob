import json

def rad_to_deg(r):
    return r * 180 / 3.141592653589793

# --- Шаг 1: Прочитать lab_row.json как строку ---
with open("lab_row.json", "r", encoding="utf-8") as f:
    raw_json_string = f.read()

# --- Шаг 2: Распаковать двойной JSON (строка внутри строки) ---
decoded_str = json.loads(raw_json_string)
parsed_response = json.loads(decoded_str)

# --- Шаг 3: Найти блок с наибольшим током (по сумме модулей IA, IB, IC) ---
max_block = None
max_sum = 0
for key, block in parsed_response.items():
    if "I" in block and isinstance(block["I"], list) and len(block["I"]) >= 3:
        current_block = block["I"]
        current_sum = sum(abs(i[0]) for i in current_block[:3])  # только 3 фазы
        if current_sum > max_sum:
            max_sum = current_sum
            max_block = current_block

# --- Шаг 4: Сохранить найденные токи в lab_data.json ---
if max_block:
    data = {
        "IA": max_block[0],
        "IB": max_block[1],
        "IC": max_block[2]
    }
    with open("lab_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("✅ Сохранены максимальные токи в lab_data.json:")
    for label, (mag, angle) in zip(["IA", "IB", "IC"], max_block):
        print(f"{label}: {mag:.3f} ∠ {rad_to_deg(angle):.2f}°")
else:
    print("❌ Не удалось найти подходящий блок токов.")
