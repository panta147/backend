from rest_framework import serializers
from job.models import JobProvider
class JobPostSErializer(serializers.ModelSerializer):
    clogo= serializers.SerializerMethodField()
    class Meta:
        model=JobProvider
        fields='__all__'
        depth = 1

        def __init__(self, *args, **kwargs):
            super(JobPostSErializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and request.method == 'POST':
                self.Meta.depth = 0
            else:
                self.Meta.depth = 1
    def get_clogo(self, obj):
        request = self.context.get('request')
        photo_url = obj.clogo.url
        return request.build_absolute_uri(photo_url)