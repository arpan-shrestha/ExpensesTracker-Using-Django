from rest_framework import serializers
from .models import ExpenseIncome
from django.contrib.auth.models import User

class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = '__all__'
        read_only_fields = ['user', 'total', 'created_at', 'updated_at']
    
    def get_total(self, obj):
        return obj.calc_total()
    
class Register(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user