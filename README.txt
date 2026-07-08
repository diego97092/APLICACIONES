# Marketplace Hub V2 - Cómo correr el programa

## 1. Abrir CMD

Ir a la carpeta del proyecto:

cd "C:\Users\Viviana\Desktop\Poyecto final crm"

## 2. Activar entorno virtual

venv\Scripts\activate

## 3. Correr backend

uvicorn backend.main:app --reload

## 4. Abrir CRM

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs

## 5. Reemplazar extensión Chrome

1. Ir a la carpeta donde tienes la extensión.
2. Reemplazar estos archivos:

- manifest.json
- background.js
- content.js
- popup.html
- popup.js

3. Verificar que los nombres queden así exactamente:

content.js
manifest.json
background.js
popup.html
popup.js

Ojo: si Windows los deja como content(2).js, popup(2).js, etc., toca renombrarlos.

## 6. Cargar extensión en Chrome

1. Abrir Chrome.
2. Ir a:

chrome://extensions/

3. Activar “Modo desarrollador”.
4. Si ya está cargada la extensión vieja:
   - darle “Quitar”
   - luego “Cargar descomprimida”
5. Seleccionar la carpeta de la extensión nueva.

## 7. Encender extensión

1. Abrir Facebook o Messenger.
2. Abrir el popup de la extensión.
3. Backend debe decir:

http://127.0.0.1:8000

4. Perfil ID:
   - Diego = 1
   - slot = 2

5. Dar click en “EXTENSIÓN APAGADA - encender”.
6. Esperar 5 segundos.
7. La extensión debe entrar a Messenger, abrir el cajón Marketplace, capturar bandeja y abrir el primer chat.

## 8. Flujo normal de trabajo

1. Correr backend.
2. Abrir CRM.
3. Abrir Facebook Messenger.
4. Encender extensión.
5. Entrar al perfil Diego o slot en el CRM.
6. Click en un chat.
7. La extensión debe buscarlo en Marketplace, hacer scroll si no está visible, abrirlo y capturar historial.

## 9. Regla importante

La extensión debe trabajar solo en:

facebook.com/messages

Nunca debe ir a:

facebook.com/marketplace

## 10. Si algo falla

Revisar:

- que el backend siga corriendo
- que la extensión esté encendida
- que el perfil ID sea correcto
- que Messenger esté abierto
- que estés en el cajón Marketplace de Messenger
- que los archivos no tengan nombres tipo content(2).js