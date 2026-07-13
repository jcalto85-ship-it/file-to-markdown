import os
import tempfile

import gradio as gr
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)

MAX_FILE_SIZE_MB = 50


def convert_to_markdown(file_path):
    if file_path is None:
        return "", None, "Sube un archivo para comenzar."

    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        return "", None, f"El archivo pesa {size_mb:.1f} MB. El límite es {MAX_FILE_SIZE_MB} MB."

    try:
        result = md.convert(file_path)
    except Exception as exc:
        return "", None, f"No se pudo convertir el archivo: {exc}"

    markdown_text = result.text_content

    original_name = os.path.splitext(os.path.basename(file_path))[0]
    out_path = os.path.join(tempfile.gettempdir(), f"{original_name}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    return markdown_text, out_path, "Conversión completa."


with gr.Blocks(title="Cualquier archivo a Markdown") as demo:
    gr.Markdown(
        """
        # 📄 ➜ 📝 Cualquier archivo a Markdown
        Sube un archivo (PDF, Word, Excel, PowerPoint, imágenes, audio, HTML, CSV, JSON, ZIP, EPub, etc.)
        y obtén su contenido convertido a Markdown.
        """
    )

    with gr.Row():
        file_input = gr.File(label="Archivo de entrada", type="filepath")

    convert_btn = gr.Button("Convertir a Markdown", variant="primary")

    status = gr.Markdown()

    with gr.Row():
        markdown_output = gr.Textbox(label="Resultado en Markdown", lines=20, show_copy_button=True)
        download_output = gr.File(label="Descargar .md")

    convert_btn.click(
        fn=convert_to_markdown,
        inputs=file_input,
        outputs=[markdown_output, download_output, status],
    )

if __name__ == "__main__":
    demo.launch()
