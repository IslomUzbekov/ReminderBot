import asyncio

from django.core.management.base import BaseCommand
from main_bot import bot


class Command(BaseCommand):
    help = 'Running bot'

    def handle(self, *args, **options):
        asyncio.run(bot.polling())
