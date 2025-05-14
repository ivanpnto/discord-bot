from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2-medium")
set_seed(42)

def generar_texto(prompt: str, max_length: int = 50) -> str:
    outputs = generator(prompt, max_length=max_length, num_return_sequences=1)
    return outputs[0]["generated_text"]

if __name__ == "__main__":
    prueba = "Hoy es un gran día porque"
    print("⏳ Cargando modelo y generando texto…")
    resultado = generar_texto(prueba, max_length=30)
    print(f"✅ Generación completada:\nPrompt: {prueba}\nGeneración: {resultado}")

