FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt
COPY mymodel
COPY main1.py.
RUN pip install-no-cache-dir-r requirements.txt I
EXPOSE 8000
CMO [uvicorn", "maini:app","hast", "0.0.0.0","port", "8000"
