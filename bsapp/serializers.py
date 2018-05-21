# -*- coding:utf-8 -*-
from rest_framework import serializers
from bsapp.models import Users, Contents, Files


class BsappSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(required = False, allow_blank = True, max_length = 100)

    psw = serializers.CharField(style = {'base_template': "ceshi.html"})

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.psw = validated_data.get('psw', instance.psw)
        instance.save()
        return instance


# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ('name', 'psw', 'phone')
