from rest_framework import fields, serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

from quiz_app.models import Quiz, Category, Answer, Question

#! Auth Serializers
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True, required=True, validators=[validate_password], style={"input_type":"password"})
    password2 = serializers.CharField(write_only = True, required=True, validators=[validate_password], style={"input_type":"password"})
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'          
        ]
        
    def create(self, validated_data):
        # print('validated_data: ', validated_data)
        password = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        # print('user: ', user)
        user.set_password(password)
        user.save()
        return user
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password' : "Password fields didn't match."})
        return data

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')
        
#! View Serializers
class CategorySerializer(serializers.ModelSerializer):
    numberOfQuizzesIncluded = serializers.SerializerMethodField()
    class Meta:  
        model = Category
        fields = ['id', 'name', 'numberOfQuizzesIncluded']
        
    def get_numberOfQuizzesIncluded(self, obj):
        return Quiz.objects.filter(category_id=obj.id).count()

class QuizSerializer(serializers.ModelSerializer):
    numberOfQuestionIncluded = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = ['title', 'numberOfQuestionIncluded']
        
    def get_numberOfQuestionIncluded(self, obj):
        return Question.objects.filter(quiz_id=obj.id).count()
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_right']
      
class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)
    difficulty = serializers.StringRelatedField()
    class Meta:
        model = Question
        fields = ['title', 'answer', 'difficulty']