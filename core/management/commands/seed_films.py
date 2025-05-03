from django.core.management.base import BaseCommand
from core.models import Film
import random

class Command(BaseCommand):
    help = 'Автоматты түрде 100 фильм қосады'

    def handle(self, *args, **kwargs):
        genres = ['Драма', 'Комедия', 'Тарихи', 'Экшн', 'Ғылыми фантастика', 'Анимация', 'Қорқынышты']
        titles = [
            'Көшпенділер', 'Томирис', 'Жаужүрек мың бала', 'Райымбек батыр', 'Аңшы', 'Сарбаздар жолы', 'Айман-Шолпан',
            'Батыр қыз', 'Жеңіс рухы', 'Көкбөрі аңызы', 'Ұлы дала', 'Қазақ хандығы', 'Түнгі күзетші', 'Ғарышқа жол',
            'Сағым жылдар', 'Аруақ', 'Естелік', 'Шыңырау', 'Қара жол', 'Тар кезең'
        ]

        Film.objects.all().delete()  # Бұрынғысын тазалау

        for i in range(100):
            title = random.choice(titles) + f" {i}"
            year = random.randint(1990, 2025)
            genre = random.choice(genres)
            description = f"{genre} жанрындағы қызықты фильм."
            rating = round(random.uniform(5.0, 9.5), 1)

            Film.objects.create(
                title=title,
                year=year,
                genre=genre,
                description=description,
                rating=rating
            )

        self.stdout.write(self.style.SUCCESS("✅ 100 фильм базаға қосылды"))
