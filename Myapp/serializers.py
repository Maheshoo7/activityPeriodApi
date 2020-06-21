from rest_framework import serializers
from .models import ActivityPeriod, User

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']

    def create(self, validated_data):
        activity_periods_data = validated_data.pop('activity_periods')
        user = User.objects.create(**validated_data)
        for activity_period_data in activity_periods_data:
            ActivityPeriod.objects.create(user=user, **activity_period_data)
        return user
