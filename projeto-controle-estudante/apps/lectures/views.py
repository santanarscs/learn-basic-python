from rest_framework import serializers, viewsets

from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'lecturer_name', 'description', 'date', 
                  'duration', 'slides_url', 'is_required']


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
