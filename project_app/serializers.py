from rest_framework import serializers
from django.contrib.auth.models import User
from project_app.models import Trip, UserProfile
from rest_framework_simplejwt.tokens import RefreshToken

class CreateTripSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Trip
        fields = ['title','description','pic','owner']
        
        
class TripUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['title','description','pic',]

class TripListSerializer(serializers.ModelSerializer):
      user = serializers.SerializerMethodField()
      def get_user(self, obj):
       return obj.user.username
      class Meta:
        model = Trip
        fields = ['title','pic','id','user']
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
       return obj.user.username
    class Meta:
        model = UserProfile
        fields = ['user','id']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password"]
    def create(self, validated_data):
        password = validated_data.pop("password")
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
        return validated_data
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)
    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")
        

        try:
            user_obj = User.objects.get(username=my_username)
            print(user_obj)
            print(my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination!")
        
        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)

        data["access"] = token
        print(data["access"])
        return data