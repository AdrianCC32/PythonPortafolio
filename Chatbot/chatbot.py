import nltk
from nltk.chat.util import Chat, reflections

# Definir los patrones y respuestas para el bot
patrones = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo puedo ayudarte?",]
    ],
    [
        r"¿cual es tu nombre\??",
        ["Mi nombre es Bot, un chatbot programado para ayudarte.",]
    ],
    [
        r"¿como estas\??",
        ["Estoy bien, ¿y tú?",]
    ],
    [
        r"(.*) (feliz|contento|bienestar)",
        ["Me alegra que estés %2.",]
    ],
    [
        r"adios",
        ["Adiós, ¡que tengas un buen día!",]
    ],
]

# Crear el bot de chat
chatbot = Chat(patrones, reflections)

# Iniciar la conversación con el bot
print("¡Hola! Soy un bot de chat. Puedes empezar a hacer preguntas o simplemente saludar.")
chatbot.converse()
