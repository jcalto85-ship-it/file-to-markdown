---
title: Cualquier Archivo A Markdown
emoji: 📝
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
---

# Cualquier archivo a Markdown

App web para convertir prácticamente cualquier archivo a Markdown, usando
[MarkItDown](https://github.com/microsoft/markitdown) (Microsoft) + [Gradio](https://gradio.app).

Formatos soportados: PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx), imágenes
(con OCR/metadatos EXIF), audio (transcripción), HTML, CSV, JSON, XML, ZIP, EPub,
texto plano y más.

## Uso local

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abre el link que aparece en la terminal (normalmente http://127.0.0.1:7860).

## Despliegue gratuito en Hugging Face Spaces (con GitHub)

Hugging Face Spaces permite alojar esta app de forma **gratuita y permanente**
(tier CPU básico, sin costo) y se puede mantener sincronizada con un repositorio
de GitHub.

### Opción A: subir directo a Hugging Face (más simple)

1. Crea una cuenta gratuita en https://huggingface.co/join
2. Ve a https://huggingface.co/new-space
3. Elige un nombre, SDK **Gradio**, hardware **CPU basic (free)**
4. Sube los archivos `app.py`, `requirements.txt` y `README.md` de esta carpeta
   (o conecta el Space a tu repo de GitHub, ver Opción B)
5. El Space construye la app automáticamente y te da una URL pública fija, p. ej.
   `https://huggingface.co/spaces/tu-usuario/tu-space`

### Opción B: mantener el código en GitHub y sincronizarlo con el Space

1. Crea un repositorio en GitHub y sube esta carpeta:
   ```bash
   git remote add origin https://github.com/tu-usuario/file-to-markdown.git
   git push -u origin main
   ```
2. Crea el Space como en la Opción A.
3. En la configuración del Space, usa "GitHub Actions" o el flujo de
   "Sync from GitHub" (Settings → Repository secrets → añade un token de HF y
   configura un workflow de GitHub Actions que haga `git push` al repo del Space
   en cada push a `main`). Hugging Face tiene una plantilla lista para esto en:
   Space → Settings → "GitHub Actions".

De esta forma, cada cambio que subas a GitHub se refleja automáticamente en la
app pública, sin costo de hosting.

## Notas

- El tamaño máximo de archivo está limitado a 50 MB en `app.py` (variable
  `MAX_FILE_SIZE_MB`) para evitar timeouts en el tier gratuito.
- La transcripción de audio y el OCR de imágenes son más lentos en el tier CPU
  gratuito; para archivos grandes puede tardar más.
