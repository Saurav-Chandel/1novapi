from rest_framework import serializers
from .models import User,Post,Article,Publication

class UserSignupSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #         required=True,
    #         validators=[UniqueValidator(queryset=User.objects.all())]
    #        )

    password = serializers.CharField(write_only=True, required=True)
    # confirm_password = serializers.CharField(write_only=True, required=True)
  
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password','otp')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['confirm_password']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            otp=validated_data['otp']
            
                  
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class OtpGenerateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','first_name','last_name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=["user",'category','bedroom','kitchen','area','amunities']


# class PublicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Publication
#         feilds="__all__"   

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Article
#         feilds="__all__"               