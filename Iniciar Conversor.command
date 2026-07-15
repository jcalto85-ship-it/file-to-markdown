#!/bin/bash
cd "$(dirname "$0")"

echo "Iniciando Conversor de Archivos a Markdown..."
./venv/bin/python app.py &
APP_PID=$!

# Espera a que el servidor esté listo y abre el navegador
for i in $(seq 1 30); do
    if curl -s -o /dev/null http://127.0.0.1:7860; then
        open http://127.0.0.1:7860
        break
    fi
    sleep 1
done

echo ""
echo "La app está corriendo. Deja esta ventana abierta mientras la uses."
echo "Para cerrarla, cierra esta ventana de Terminal."
wait $APP_PID
