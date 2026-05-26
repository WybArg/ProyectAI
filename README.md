# Proyecto IA - Entorno de Desarrollo Guiado por Reglas

¡Bienvenido al proyecto! Este espacio de trabajo está diseñado y configurado específicamente para interactuar con asistentes de Inteligencia Artificial (IA) bajo un conjunto estricto de directrices de desarrollo y estilo de programación.

El objetivo principal de este entorno es garantizar la producción de código altamente legible, modular, autodocumentado y fácil de mantener.

---

## 🛠️ ¿Qué hace este Proyecto?

Este repositorio sirve como un **entorno de desarrollo controlado y estandarizado**. Su función es:
1. **Establecer reglas claras de codificación:** Mediante archivos de reglas que la IA debe leer activamente antes de generar cualquier script.
2. **Modularizar el desarrollo:** Forzar a que los programas se dividan en scripts pequeños y funcionales (menos de 200 líneas).
3. **Autodocumentar el código:** Exigir comentarios exhaustivos en cada línea para asegurar que cualquier persona (o la propia IA en futuras interacciones) pueda comprender el flujo exacto de ejecución sin ambigüedades.
4. **Contextualizar cada script:** Proveer encabezados explicativos al inicio de cada archivo para entender de inmediato su rol dentro del sistema.

---

## 📄 Estructura del Workspace

* **`rules.md`**: El archivo principal que contiene las reglas de programación para la IA. Es el contrato de desarrollo.
* **`.cursorrules`**: Archivo de configuración para asistentes de IA (como Cursor, Copilot u otros agentes) que carga automáticamente las directrices del proyecto en su contexto.
* **`README.md`**: Este archivo, que documenta el propósito y funcionamiento general del espacio de trabajo.

---

## 📋 Resumen de las Reglas Activas

1. 📏 **Límite de 200 líneas:** Ningún script de código puede exceder las 200 líneas de longitud.
2. 💬 **Comentarios línea por línea:** Cada línea de código que se escriba debe llevar un comentario a su derecha o arriba explicando qué hace.
3. ✍️ **Encabezado obligatorio:** Todo archivo de código debe iniciar con un comentario explicativo que detalla su función.

---

## 🚀 Cómo empezar

1. Crea tus archivos de código (Python, JavaScript, etc.) en este directorio.
2. Al interactuar con tu asistente de IA, este leerá automáticamente `.cursorrules` y `rules.md` para cumplir con las directrices.
3. ¡Disfruta de un código limpio, modular y perfectamente documentado!
