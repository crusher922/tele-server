#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from telethon import TelegramClient, events

def main():
    """Run administrative tasks."""
    api_id = 24587662
    api_hash = 'eb9d992d7a73c15b6d0acfd6f2e9c1c4'

    # Crea el cliente
    client = TelegramClient('session_name', api_id, api_hash)

    # Función para reenviar mensajes
    async def reenviar_mensaje(message, chat_destino):
        # Reenvía el mensaje
        await client.send_message(chat_destino, message)

    # Escucha nuevos mensajes en el chat origen
    @client.on(events.NewMessage)
    async def main(event):
        # Reemplaza con el ID del chat origen
        chat_origen = [927606242, -1001291285712, 906218834, -4104859139, -1001629605754, -1001179560361, 6485295670]

        # Reemplaza con el ID del chat destino
        chat_destino = -4106805637

        if event.chat_id in chat_origen:
            await reenviar_mensaje(event.message, chat_destino)

    # Inicia el bucle de eventos del cliente
    client.start()
    client.run_until_disconnected()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
