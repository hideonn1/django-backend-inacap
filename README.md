# Panoramas Proyecto - Programación Backend INACAP

Este repositorio contiene el proyecto desarrollado para la asignatura de **Programación Backend** de **INACAP**. Su propósito es registrar, practicar y demostrar los contenidos y avances vistos en clases, utilizando el lenguaje **Python** y el framework web **Django**.

---

## 🛠️ Tecnologías y Versiones

- **Lenguaje:** Python `3.13` (compatible con `>= 3.10`)
- **Framework Web:** Django `6.1`
- **Base de Datos:** SQLite 3 (por defecto para entorno de desarrollo)
- **Servidor WSGI:** Gunicorn
- **Contenedores:** Docker & Docker Compose

---

## 🚀 Instalación y Ejecución

Puedes ejecutar este proyecto en **cualquier sistema operativo** (Windows, macOS o Linux) utilizando un entorno virtual tradicional o mediante Docker.

### Prerrequisitos

- Tener instalado [Git](https://git-scm.com/).
- **Opción A (Recomendada si usas Python local):** [Python 3.10+](https://www.python.org/downloads/).
- **Opción B (Recomendada para aislamiento total):** [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

---

### 1. Clonar el Repositorio

Abre una terminal o línea de comandos y ejecuta:

```bash
git clone https://github.com/hideonn1/panoramasProyecto.git
cd panoramasProyecto
```

---

### 2. Opción A: Ejecución con Entorno Virtual Local

#### **Paso 1: Crear y activar el entorno virtual**

- **En Windows (PowerShell / CMD):**
  ```powershell
  # Crear entorno virtual
  python -m venv venv

  # Activar en PowerShell
  .\venv\Scripts\Activate.ps1

  # O si usas CMD:
  .\venv\Scripts\activate.bat
  ```

- **En Linux / macOS (Bash / Zsh):**
  ```bash
  # Crear entorno virtual
  python3 -m venv venv

  # Activar
  source venv/bin/activate
  ```

#### **Paso 2: Instalar dependencias**

Con el entorno virtual activado, instala Django y las dependencias necesarias:

```bash
pip install Django gunicorn
```

#### **Paso 3: Aplicar migraciones**

```bash
# En Windows / Linux / macOS (con venv activo):
python manage.py migrate
```

#### **Paso 4: Iniciar el servidor de desarrollo**

```bash
python manage.py runserver
```

Abre tu navegador web y visita: [http://localhost:8000](http://localhost:8000) (o [http://127.0.0.1:8000](http://127.0.0.1:8000)).

---

### 3. Opción B: Ejecución con Docker (Multiplataforma)

Si tienes Docker instalado, no necesitas configurar Python en tu máquina anfitriona.

#### **Iniciar el contenedor con Docker Compose:**

```bash
docker compose up --build
```

*(O `docker-compose up --build` según la versión de Docker instalada).*

El proyecto estará disponible automáticamente en [http://localhost:8000](http://localhost:8000).

Para detener el contenedor:
```bash
docker compose down
```

---

## 📁 Estructura del Proyecto

```text
panoramasProyecto/
├── manage.py              # Script principal de gestión de Django
├── panoramasProyecto/     # Configuración global del proyecto (settings, urls, wsgi)
├── panoramasApp/          # Aplicación principal del proyecto
├── templates/             # Plantillas HTML
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── Dockerfile             # Definición de la imagen Docker
├── docker-compose.yml     # Orquestación de contenedores
└── README.md              # Documentación del proyecto
```

---

## 📌 Comandos Útiles

- **Crear un superusuario (Administrador):**
  ```bash
  python manage.py createsuperuser
  ```
- **Crear nuevas migraciones tras modificar modelos:**
  ```bash
  python manage.py makemigrations
  ```
- **Aplicar migraciones pendientes:**
  ```bash
  python manage.py migrate
  ```
