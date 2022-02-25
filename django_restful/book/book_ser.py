from . import models
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ["name", "price", "publish_time", "publish"]
        model = models.Book
        # 对字段的额外要求
        extra_kwargs = {
        }
