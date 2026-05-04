# Blog Django

Proyecto de blog desarrollado con Django 6, que incluye publicaciones con editor de texto enriquecido, autenticación de usuarios, perfiles y mensajería interna entre usuarios.

---

## Características

- **Publicaciones:** listado paginado, detalle, creación, edición y eliminación de posts con imagen opcional.
- **Editor enriquecido:** integración de CKEditor 5 para el contenido de las publicaciones.
- **Buscador:** búsqueda de publicaciones por título integrada en el listado.
- **Permisos:** solo el autor de una publicación puede editarla o eliminarla.
- **Autenticación:** registro, inicio/cierre de sesión y cambio de contraseña.
- **Perfiles:** cada usuario tiene un perfil con avatar, biografía y fecha de nacimiento. Se crea automáticamente al registrarse.
- **Mensajería interna:** bandeja de entrada, mensajes enviados, redacción, lectura y eliminación de mensajes entre usuarios.
- **Panel de administración** de Django habilitado.

---

## Tecnologías

| Paquete | Versión |
|---|---|
| Python | 3.14 |
| Django | 6.0.4 |
| django-ckeditor-5 | 0.2.20 |
| django-widget-tweaks | 1.5.1 |
| Pillow | 12.2.0 |
| SQLite | (base de datos por defecto) |

---

## Estructura del proyecto

```
blog_django/
├── entorno/                  # Entorno virtual
└── blog_proyecto/            # Proyecto Django
    ├── blog/                 # App principal de publicaciones
    │   ├── models.py         # Modelo Publicacion
    │   ├── views.py          # Vistas (función y clase) con paginación y permisos
    │   ├── urls.py
    │   ├── forms.py
    │   └── templates/blog/
    ├── cuentas/              # App de autenticación y perfiles
    │   ├── models.py         # Modelo Perfil (OneToOne con User)
    │   ├── signals.py        # Crea el Perfil automáticamente al registrar un User
    │   ├── apps.py           # Activa las signals al iniciar la app
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/cuentas/
    ├── mensajeria/           # App de mensajes internos
    │   ├── models.py         # Modelo Mensaje
    │   ├── views.py          # Bandeja, enviados, redactar, ver y eliminar
    │   ├── forms.py          # Formulario de redacción
    │   ├── urls.py
    │   └── templates/mensajeria/
    ├── blog_proyecto/        # Configuración del proyecto
    │   ├── settings.py
    │   └── urls.py
    ├── media/                # Archivos subidos por usuarios
    ├── static/
    ├── manage.py
    └── requirements.txt
```

---

## URLs principales

| URL | Descripción |
|---|---|
| `/` | Página de inicio |
| `/lista/` | Listado paginado de publicaciones con buscador |
| `/publicacion/<pk>/` | Detalle de una publicación |
| `/crear/` | Crear nueva publicación *(requiere login)* |
| `/editar/<pk>/` | Editar publicación *(solo el autor)* |
| `/eliminar/<pk>/` | Eliminar publicación *(solo el autor)* |
| `/about/` | Acerca de |
| `/cuentas/registro/` | Registro de usuario |
| `/cuentas/login/` | Inicio de sesión |
| `/cuentas/logout/` | Cerrar sesión |
| `/cuentas/perfil/` | Ver perfil |
| `/cuentas/perfil/editar/` | Editar perfil |
| `/cuentas/perfil/contrasena/` | Cambiar contraseña |
| `/mensajeria/bandeja/` | Bandeja de entrada |
| `/mensajeria/enviados/` | Mensajes enviados |
| `/mensajeria/enviar/` | Redactar nuevo mensaje |
| `/mensajeria/ver/<pk>/` | Leer un mensaje |
| `/mensajeria/eliminar/<pk>/` | Eliminar un mensaje |
| `/admin/` | Panel de administración |

---

## Modelos principales

**Publicacion** (`blog/models.py`)

| Campo | Tipo |
|---|---|
| `titulo` | CharField |
| `resumen` | CharField |
| `categoria` | CharField con choices (Tecnología, Cultura, Opinión, Ciencia, Otro) |
| `contenido` | CKEditor5Field |
| `autor` | ForeignKey (User) — se asigna automáticamente al usuario logueado |
| `imagen` | ImageField (opcional) |
| `fecha` | DateTimeField (auto) |

**Perfil** (`cuentas/models.py`)

| Campo | Tipo |
|---|---|
| `usuario` | OneToOneField (User) |
| `avatar` | ImageField (opcional) |
| `biografia` | TextField |
| `fecha_nacimiento` | DateField |

**Mensaje** (`mensajeria/models.py`)

| Campo | Tipo |
|---|---|
| `remitente` | ForeignKey (User) — se asigna automáticamente al usuario logueado |
| `destinatario` | ForeignKey (User) |
| `asunto` | CharField |
| `contenido` | TextField |
| `fecha` | DateTimeField (auto) |
| `leido` | BooleanField (se marca `True` automáticamente al abrir el mensaje) |







