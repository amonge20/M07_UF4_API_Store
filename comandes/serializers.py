# comandes/serializers.py
from rest_framework import serializers
from .models import Comanda

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'
>>>>>>> origin/Estructura
