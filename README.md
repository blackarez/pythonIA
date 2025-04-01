# API FastAPI

Este es un proyecto básico de API REST utilizando FastAPI.

## Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
   ```bash
   python -m venv .venv
   ```
3. Activar el entorno virtual:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```
4. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar la aplicación:

```bash
python main.py
```

O alternativamente:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Documentación

- Documentación de la API: `http://localhost:8000/docs`
- Documentación alternativa: `http://localhost:8000/redoc`

## Endpoints

- GET `/`: Mensaje de bienvenida
- GET `/items/{item_id}`: Obtener información de un item por ID 