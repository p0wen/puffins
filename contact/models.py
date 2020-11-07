from django.db import models


class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('1', 'General'),
        ('2', 'Return'),
        ('3', 'Pre Order'),
        ('4', 'Delivery'),
        ('5', 'Payment'),
    ]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=120, null=True, blank=False)
    title = models.CharField(max_length=120, null=True, blank=False)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ["category"]

    def __str__(self):
        return self.title
