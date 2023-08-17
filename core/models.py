from django.db import models


class User(models.Model):
    phone_number = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        verbose_name="Номер телефона пользователя",
    )
    check_code = models.CharField(
        max_length=4,
        null=False,
        blank=False,
        verbose_name="Код авторизации пользователя",
    )
    invite_key = models.CharField(
        max_length=6, null=False, blank=False, verbose_name="Инвайт-код авторизации"
    )
    referral_link = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Реферальная ссылка пользователя",
    )

    created_dt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создание пользователя"
    )
    updated_dt = models.DateTimeField(
        auto_now=True, verbose_name="Время последнего обновления пользователя"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь: {self.phone_number}; время создание: {self.created_dt}"
