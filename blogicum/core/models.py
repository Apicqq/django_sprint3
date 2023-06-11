from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано',
                                       help_text='Снимите галочку,'
                                                 ' чтобы скрыть публикацию.')

    class Meta:
        abstract = True


class TimeCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')

    class Meta:
        abstract = True


class SortingModel(models.Model):
    class Meta:
        # Не уверен, по какому полю тут нужна сортировка, пусть будет по дате.
        ordering = ['-pub_date']
        abstract = True
