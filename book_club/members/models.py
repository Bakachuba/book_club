import uuid

from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Карточка участника книжного клуба
class MemberCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100, unique=True,
                                   default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Library card of ({self.user}), Card number: ({self.card_number})"
