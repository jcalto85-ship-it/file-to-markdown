---
title: Cualquier Archivo A Markdown
emoji: 📝
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 6.20.0
app_file: app.py
pinned: false
---

# Cualquier archivo a Markdown

App web para convertir prácticamente cualquier archivo a Markdown, usando
[MarkItDown](https://github.com/microsoft/markitdown) (Microsoft) + [Gradio](https://gradio.app).

Formatos soportados: PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx), audio
(transcripción), HTML, CSV, JSON, XML, ZIP, EPub, texto plano y más.

Para imágenes, por defecto solo se extraen sus metadatos EXIF (MarkItDown no
incluye OCR nativo). Si el usuario ingresa su propia API key de OpenAI en las
"Opciones avanzadas" de la interfaz, además se genera una descripción del
contenido visual usando `gpt-4o-mini`. La key no se guarda ni se comparte: solo
se usa en memoria para esa conversión.

## Uso local (recomendado)

Pensada para uso personal en tu Mac: 100% gratis, sin depender de internet ni
de límites de un hosting gratuito.

**Forma fácil:** haz doble clic en `Iniciar Conversor.command`. Abre una
ventana de Terminal, levanta el servidor y abre tu navegador en
http://127.0.0.1:7860 automáticamente. Deja esa ventana abierta mientras la
uses; cerrarla apaga el servidor.

**Forma manual:**
```bash
./venv/bin/python app.py
```
Abre http://127.0.0.1:7860 en tu navegador.

## Despliegue en la nube (opcional)

Este repo también está preparado para desplegarse en
[Render](https://render.com) (Web Service, tier Free, build command
`pip install -r requirements.txt`, start command `python app.py`), conectado a
este mismo repo de GitHub. Es gratuito, pero el tier Free de Render solo
asigna 0.1 vCPU, lo que provoca fallas intermitentes de conexión durante la
conversión (ocasionalmente hay que reintentar). Para uso personal, se
recomienda la versión local de arriba en su lugar.

(Nota: Hugging Face Spaces ya no permite Gradio en su tier gratuito — ahora
requiere una suscripción PRO — por eso no es una opción aquí.)

## Notas

- El tamaño máximo de archivo está limitado a 50 MB en `app.py` (variable
  `MAX_FILE_SIZE_MB`).
- La transcripción de audio y el OCR de imágenes son más lentos; para
  archivos grandes puede tardar más.
