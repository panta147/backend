from rest_framework import serializers
from job.models import JobProvider
class JobPostSErializer(serializers.ModelSerializer):
    class Meta:
        model=JobProvider
        fields='__all__'