from rest_framework import serializers
from .models import Listing, Review

class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'location']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    listing = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__' 
