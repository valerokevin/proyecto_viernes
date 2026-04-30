from fastapi import FastAPI, HTTPException

# ============================================
# CONFIGURACIÓN
# ============================================

MESSAGES: dict[str, str] = {
    "es": "Hola {name}, gracias por confiar en nuestros servicios de DJ y sonido.",
    "en": "Hello {name}, thank you for choosing our DJ and sound services.",
    "fr": "Bonjour {name}, merci de faire confiance à nos services DJ et son."
}

SUPPORTED_LANGUAGES = list(MESSAGES.keys())

# ============================================
# APP
# ============================================

app = FastAPI(
    title="DJ Sound & Lights API",
    description="API para gestión de eventos, sonido y luces",
    version="1.0.0"
)

# ============================================
# RF-01: INFO API
# ============================================

@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "DJ Sound & Lights API",
        "version": "1.0.0",
        "domain": "events-entertainment"
    }

# ============================================
# RF-02: BIENVENIDA
# ============================================

@app.get("/client/{name}")
async def welcome_client(
    name: str,
    language: str = "es"
) -> dict[str, str]:

    template = MESSAGES.get(language, MESSAGES["es"])
    message = template.format(name=name)

    return {
        "message": message,
        "client": name,
        "language": language if language in MESSAGES else "es"
    }

# ============================================
# RF-03: INFORMACIÓN DE EVENTO
# ============================================

@app.get("/event/{event_id}/info")
async def event_info(
    event_id: str,
    detail_level: str = "basic"
) -> dict:

    basic_info = {
        "event_id": event_id,
        "type": "fiesta",
        "status": "programado"
    }

    if detail_level == "full":
        basic_info.update({
            "client": "Juan Pérez",
            "location": "Bogotá",
            "equipment": ["luces LED", "sonido profesional", "DJ controller"],
            "duration": "6 horas"
        })

    return basic_info

# ============================================
# RF-04: SERVICIO SEGÚN HORARIO
# ============================================

@app.get("/service/schedule")
async def service_schedule(hour: int) -> dict:

    if hour < 0 or hour > 23:
        raise HTTPException(status_code=400, detail="Hora inválida (0-23)")

    if 8 <= hour <= 17:
        return {
            "message": "Horario administrativo - Reservas y atención",
            "services": ["bookings", "clients"]
        }
    elif 18 <= hour <= 23:
        return {
            "message": "Horario de eventos - Servicio activo",
            "services": ["events", "DJ en vivo", "luces y sonido"]
        }
    else:
        return {
            "message": "Fuera de servicio",
            "services": []
        }

# ============================================
# RF-05: HEALTH CHECK
# ============================================

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "domain": "DJ Sound & Lights"
    }