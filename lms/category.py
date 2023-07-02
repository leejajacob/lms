import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')
django.setup()

from books.models import Genre

# Create and save Genre objects
genre1 = Genre(name='Fiction')
genre1.save()

genre2 = Genre(name='Thriller')
genre2.save()

genre3 = Genre(name='Mystery')
genre3.save()

genre4 = Genre(name='Drama')
genre4.save()

genre5 = Genre(name='Action')
genre5.save()

genre6 = Genre(name='Romance')
genre6.save()

genre7 = Genre(name='Horror')
genre7.save()

