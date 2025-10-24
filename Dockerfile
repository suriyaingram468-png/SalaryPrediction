FROM python:3.9-slim

WORKDIR /app

# Update package lists and install required packages
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     gcc \
#     python3-dev \
#     && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Command to run the application
CMD ["python", "app.py"]

# FROM python:3.9-slim
# WORKDIR /app
# RUN apt-get update --fix-missing && \
#     apt-get install -y --no-install-recommends \
#     libgomp1 && \
#     rm -rf /var/lib/apt/lists/*
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# CMD ["python", "app.py"]

# # FROM python:3.9-slim
# # WORKDIR /app
# # COPY . .
# # RUN pip install --no-cache-dir -r requirements.txt
# # EXPOSE 5000
# # ENV MODEL_FILE=salary_predictor.joblib
# # CMD ["streamlit", "run", "streamlit_app.py"]