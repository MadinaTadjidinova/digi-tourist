import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Добавляем корень проекта в sys.path

import json
from dotenv import load_dotenv
from db_loader import load_all_cafe_data  # теперь сработает корректно

from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
docs = []

for file in os.listdir("db"):
    if file.endswith(".json"):
        with open(f"db/{file}", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"❌ Ошибка чтения {file}: {e}")
                continue

            # Если это список (например, отели)
            if isinstance(data, list):
                for entry in data:
                    if not isinstance(entry, dict):
                        continue
                    name = entry.get("name", "Без названия")
                    type_ = entry.get("type", "")
                    address = entry.get("location", "") if isinstance(entry.get("location"), str) else entry.get("location", {}).get("address", "")
                    description = entry.get("description", "")
                    rating = entry.get("rating", "")
                    services = ", ".join(entry.get("services", []))
                    content = f"{name} — {type_}, {address}\nРейтинг: {rating}\nУслуги: {services}\nОписание: {description}"
                    docs.append(Document(page_content=content, metadata={"source": name}))

            # Если это словарь (например, кафе)
            elif isinstance(data, dict):
                name = data.get("name", "Без названия")
                type_ = data.get("type", "")
                address = data.get("location", {}).get("address", "")
                content = f"{name} — {type_}, {address}\n"

                if "reviews_summary" in data:
                    content += f"Отзывы: {data['reviews_summary']}\n"

                if "menu" in data:
                    menu_data = data.get("menu", [])

                    if isinstance(menu_data, dict):
                        for category, items in menu_data.items():
                            content += f"\n\n{category}:\n"
                            for item in items:
                                item_name = item.get("name", "")
                                price = item.get("price_som") or item.get("price") or ""
                                content += f"{item_name} - {price} с\n"

                    elif isinstance(menu_data, list):
                        content += "\n".join([
                            f"{item.get('name', '')} - {item.get('price_som', item.get('price', ''))} с"
                            for item in menu_data
                        ])

                    elif isinstance(menu_data, str):
                        content += f"\nМеню: {menu_data}\n"

                docs.append(Document(page_content=content, metadata={"source": name}))

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
vectorstore.save_local("vector_index")
print("✅ Векторизация завершена успешно.")
