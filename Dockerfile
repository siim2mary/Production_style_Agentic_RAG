# 1. Use an official Python slim image for a small, fast production footprint
FROM python:3.10-slim

# 2. Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install system dependencies
# build-essential is required for FAISS; libmagic-dev is for file type detection
RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements first to leverage Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your application code (including config.py and main.py)
COPY . .

# 7. Create the directories used in config.py if they don't exist
RUN mkdir -p temp_uploads faiss_index

# 8. Expose the port (Railway uses this as a hint, but assigns its own)
EXPOSE 8000

# 9. Start the application using uvicorn
# We use sh -c to allow the $PORT environment variable from Railway to be injected
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]