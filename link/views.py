from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *

class LinkView(generics.ListAPIView):
    """
    获取链接列表
    """
    model = Link
    serializer_class = LinkSerializer
    pagination_class = None
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Link.objects.filter(label=self.kwargs['label'], is_active=True)
