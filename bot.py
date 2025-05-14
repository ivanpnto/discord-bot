import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import yt_dlp as youtube_dl
from gpt2_module import generar_texto

# Carga variables de entorno
load_dotenv(override=True)  # OBLIGATORIO si estás actualizando el .env
token = os.getenv("TOKEN")

print("DEBUG Token:", token)
print("DEBUG Longitud:", len(token) if token else None)
print("TOKEN cargado?", "Sí" if token else "No")

# Ruta al ejecutable ffmpeg
FFMPEG_PATH = r"C:\Users\ivanp\OneDrive\Documentos\ffmpeg\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"

# Opciones de yt-dlp para extraer solo el mejor audio
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegAudioConvertor',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Configuración de intents y bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user} (ID: {bot.user.id})")

@bot.command()
async def ayuda(ctx):
    help_text = """
    **Comandos disponibles:**
    - !hola: El bot responderá con un saludo al usuario.
    - !info: Responde con la informacion basica de dev.
    - !musica: El bot recibe como argumento la URL a poner.
    - !parar: Detiene la musica y desconecta al bot.
    """
    await ctx.send(help_text)

@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola {ctx.author.mention}! Soy BotPy.")

@bot.command()
async def info(ctx):
    bot_info = """
    Soy un bot creado por Ivan_Pma21
    Version: 1.3.3
    """
    await ctx.send(bot_info)

@bot.command()
async def musica(ctx, *, url: str):
    if not ctx.author.voice:
        return await ctx.send("❌ Entra en un canal de voz primero.")
    vc = ctx.guild.voice_client
    if vc and vc.is_playing():
        vc.stop()
    if not vc or not vc.is_connected():
        vc = await ctx.author.voice.channel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']

    vc.play(
        discord.FFmpegPCMAudio(
            audio_url,
            executable=FFMPEG_PATH,
            before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            options='-vn'
        )
    )
    await ctx.send(f"▶ Reproduciendo: **{info.get('title','desconocido')}**")

@bot.command()
async def parar(ctx):
    """Detiene la reproducción y desconecta al bot."""
    vc = ctx.guild.voice_client
    if not vc or not vc.is_connected():
        return await ctx.send("❌ No estoy conectado a ningún canal de voz.")
    if vc.is_playing():
        vc.stop()
    await vc.disconnect()
    await ctx.send("⏹ Música detenida y desconectado del canal de voz.")

@bot.command()
async def chat(ctx, *, mensaje: str):
    """Responde usando GPT-2 local."""
    await ctx.trigger_typing()
    respuesta = generar_texto(mensaje, max_length=100)
    contenido = respuesta[len(mensaje):].strip()
    await ctx.send(contenido)

if __name__ == '__main__':
    bot.run(token)
