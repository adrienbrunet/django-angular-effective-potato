from rest_framework import serializers

from .models import Child, Parent


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = ('pk', 'name', )


class ChildSerializer(serializers.ModelSerializer):
    # parent = ParentSerializer()

    class Meta:
        model = Child
        fields = ('pk', 'parent', )
