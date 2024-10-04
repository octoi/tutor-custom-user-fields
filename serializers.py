from rest_framework import serializers
from django.contrib.auth import get_user_model
from openedx.core.djangoapps.user_api.accounts.serializers import UserReadOnlySerializer
from student.models import UserProfile

User = get_user_model()

class CustomUserSerializer(UserReadOnlySerializer):
    address = serializers.CharField(source='profile.address', required=False, allow_blank=True)
    place = serializers.CharField(source='profile.place', required=False, allow_blank=True)
    pincode = serializers.CharField(source='profile.pincode', required=False, allow_blank=True)

    class Meta(UserReadOnlySerializer.Meta):
        model = User
        fields = UserReadOnlySerializer.Meta.fields + ('address', 'place', 'pincode')
        read_only_fields = ('username', 'email', 'date_joined')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        
        # Update UserProfile fields
        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        
        return super(CustomUserSerializer, self).update(instance, validated_data)