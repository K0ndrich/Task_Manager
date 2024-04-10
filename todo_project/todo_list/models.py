from django.db import models


class ToDo(models.Model):
    title = models.CharField("Название Задания", max_length=500)
    is_complete = models.BooleanField("Завершено", default=False)
    user = models.CharField("name",max_length=50,default="")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title
