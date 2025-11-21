from django.core.management.base import BaseCommand
from main.models import MotivationalQuote

class Command(BaseCommand):
    help = 'Load default motivational quotes'

    def handle(self, *args, **kwargs):
        quotes = [
            "Code is like humor. When you have to explain it, it’s bad.",
            "First, solve the problem. Then, write the code.",
            "Experience is the name everyone gives to their mistakes.",
            "In order to be irreplaceable, one must always be different.",
            "Java is to JavaScript what car is to Carpet.",
            "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday’s code."
        ]

        for q in quotes:
            MotivationalQuote.objects.get_or_create(text=q)

        self.stdout.write(self.style.SUCCESS("✅ Default quotes loaded successfully!"))
