from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer

# from somewhere import handle_uploaded_file


def handle_uploaded_file(*args, **kwargs):
    pass


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def upload_file(self):
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES["file"])
                return HttpResponseRedirect("/success/url/")
        else:
            form = UploadFileForm()
        return render(request, "upload.html", {"form": form})

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def object_instance(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])

    def perform_create(self, serializer):
        serializer.data.owner = self.request.user
        super().perform_create(serializer)

    def has_permission(self, request, view):
        self.check_object_permissions(self.request, obj)

    def has_object_permission(self, request, view, obj):
        self.check_object_permissions(self.request, obj)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
