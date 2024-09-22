from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # Show the username or string representation of the actor
    target = serializers.SerializerMethodField()  # Custom field for the target object

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'is_read']

    def get_target(self, obj):
        # Return a string representation of the target object
        return str(obj.target)