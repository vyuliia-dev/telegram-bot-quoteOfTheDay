FROM ubuntu:22.04

# Устанавливаем Python и pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запуск бота
CMD ["python3", "main.py"]
