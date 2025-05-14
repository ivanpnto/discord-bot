**📄 Descripción**

Este proyecto es un bot de Discord en Python que combina funcionalidades de reproducción de música, comandos básicos y un módulo de generación de texto con GPT-2 ejecutado localmente. Está diseñado para ser fácil de desplegar y extender, usando discord.py para la interacción con Discord, yt-dlp y FFmpeg para audio, y Hugging Face Transformers para IA local.

**🚀 Características principales**

- !hola saluda al usuario.
- !ayuda muestra la lista de comandos disponibles. 

Reproducción de música:

- !musica <URL> reproduce audio de YouTube en el canal de voz.
- !parar detiene la reproducción y desconecta al bot. 

Chat IA local:

- !chat <mensaje> genera respuestas con GPT-2 Medium sin necesidad de API key ni coste por mensaje. 

**📁 Estructura de archivos**

bot_ds/
 ├── bot.py               # Punto de entrada: define eventos y comandos de Discord  
 ├── gpt2_module.py       # Carga GPT-2 Medium y función generar_texto()  
 ├── test.py              # Script de prueba independiente  
 ├── .gitignore           # Excluye entornos virtuales y secretos  
 └── .env                 # Variables de entorno (no subir a GitHub)  

**🛠️ Instalación y configuración**

Clonar repositorio

git clone https://github.com/ivanpnto/discord-bot.git
cd discord-bot

Crear y activar entorno virtual

python -m venv venv311              # crea entorno (≈1 GB para GPT-2 Medium)  
.\venv311\Scripts\activate          # Windows PowerShell/CMD :contentReference[oaicite:6]{index=6} 

Instalar dependencias

pip install -r requirements.txt     # incluye discord.py, yt-dlp, torch, transformers :contentReference[oaicite:7]{index=7}  

Copia .env.example a .env y añade tu token de bot:

DISCORD_TOKEN=TU_BOT_TOKEN_AQUI
Nunca subas .env ni tu token a repos públicos.

**▶️ Uso**
Arrancar el bot:

python bot.py
Comandos en Discord:

!hola → El bot responde con un saludo.

!ayuda → Muestra todos los comandos.

!musica https://youtu.be/... → Se une al canal de voz y reproduce la pista.

!parar → Detiene y desconecta.

!chat ¿Cómo estás? → Genera respuesta IA local 

**🙋 Autor**
Desarrollado por **Iván Pinto** como proyecto personal de **Ingeniería Informática**.
