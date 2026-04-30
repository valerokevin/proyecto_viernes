# ============================================
# DOCKERFILE - API DJ Sound & Lights
# ============================================

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

# Instalar uv (gestor moderno de dependencias)
RUN pip install --no-cache-dir uv

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev

# Copiar el proyecto
COPY . .

# Puerto de FastAPI
EXPOSE 8000

# Ejecutar la API
CMD ["uv", "run", "fastapi", "dev", "src/main.py", "--host", "0.0.0.0"]