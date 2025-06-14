import json
import os

def load_all_cafe_data(folder='db'):
    all_data = []

    for file in os.listdir(folder):
        if file.endswith(".json"):
            path = os.path.join(folder, file)
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        all_data.append(data)
                    elif isinstance(data, list):
                        all_data.extend(data)
            except Exception as e:
                print(f"❌ Ошибка при загрузке {file}: {e}")

    return all_data
