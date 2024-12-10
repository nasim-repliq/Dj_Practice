# Validation: Field Level, Object Level, Validators

# Field Level Validation
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 100)
    roll = serializers.Integerfield()
    name = serializers.CharField(max_length= 100)

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    
#Object Level Validation
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 100)
    roll = serializers.Integerfield()
    name = serializers.CharField(max_length= 100)

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
    

# Validators
from rest_framework import serializers
def starts_with_r(value):
    if value['0'].lower()!= 'r':
        raise serializers.ValidationError('Name should start with R')
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 100, validators=[starts_with_r])
    roll = serializers.Integerfield()
    name = serializers.CharField(max_length= 100)
