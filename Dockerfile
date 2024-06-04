# Dockerfile

# 使用Python官方映像
FROM python:3.10

# 設定工作目錄
WORKDIR /app

# 複製應用程式文件到容器
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./src /app/src

# 設定啟動容器時要執行的指令
CMD alembic upgrade head;uvicorn src.main:app --host 0.0.0.0 --port 8000