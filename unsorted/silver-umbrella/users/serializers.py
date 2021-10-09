from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.serializers import ModelSerializer

from users.models import Profile


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        context = {"request": request}
        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
