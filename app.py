# IMPORTANTE:
# Recuerda leer la documentación
# el comando que te dan para iniciar el servidor:
# uvicorn main:app --reload
# te permite que se autoactualice


from fastapi import FastAPI

# Con '.' accedemos a los archivos dentro de una carpeta.
# Traemos al modulo "user", que es una constante que creamos
from routes.user import user

app = FastAPI(

    # La documentación de una api es necesaria para permitirle al desarrllador frontend
    # entender cómo funciona la api y qué puede esperar

    title="My api",  # Por default: FastAPI
    description="This api is for testing purposes only",
    version="0.0.1",

    openapi_tags=[
        {
            "name": "users",    # Ya lo tienes que tener asignado a este nombre a los tags en tus routes
            "description": "users routes"
        }   # Puedes seguir añadiendo etiquetas que hayas definido a tus rutas
            # y agregarles la propiedad description. Pero debes crear otro diccionario seguido
            # a este
    ]


)

# Habiendo importado user, ahora llamamos
# al método que app tiene guardado
# con él indicaremos que incluiremos un ruta
# configurada en un archivo externos
app.include_router(user)

# si el archivo queda con las dos lineas: import y la definición de app = FastAPI() devolverá un notfound