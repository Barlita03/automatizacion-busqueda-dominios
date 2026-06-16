# Buscador de Dominios Automatizado 🚀

Este proyecto es un script en Python diseñado para verificar la disponibilidad de múltiples nombres de dominio `.com` de forma automática y masiva utilizando consultas WHOIS.

## 📌 Requisitos

Asegúrate de tener instalado Python en tu computadora. Luego, instala la dependencia necesaria ejecutando:

```bash
pip install python-whois
```

## ⚙️ ¿Cómo usarlo?

1. **Agrega tus ideas de dominios:** Escribe los dominios que quieras verificar en el archivo `propuestas_dominios.txt` (uno por línea).
2. **Ejecuta el script:** Corre el script principal desde tu terminal:
   ```bash
   python verificador_dominios.py
   ```
3. **Revisa los resultados:** El script generará un archivo llamado `dominios_disponibles.md` con la lista de los dominios que están 100% libres y listos para ser registrados.

*Nota: El script incluye una pausa intencional de 2 segundos entre cada consulta para evitar que los servidores WHOIS bloqueen tu conexión por exceso de peticiones.*

¡Feliz búsqueda de dominios! 🌐
