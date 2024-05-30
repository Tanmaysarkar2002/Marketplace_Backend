from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Require authentication for most actions

from .models import Listing, Review
from .serializers import ListingSerializer, ReviewSerializer


class ListingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, key=None):
        if key is None:
            listings = Listing.objects.all()
            serializer = ListingSerializer(listings, many=True)
            return Response(serializer.data)
        else:
            try:
                listing = Listing.objects.get(pk=key)
                serializer = ListingSerializer(listing)
                return Response(serializer.data)
            except Listing.DoesNotExist:
                return Response({'error': 'Listing not found'}, status=404)

    def post(self, request):
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)  # Set the current user as the listing creator
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ReviewListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, listing_key):
        try:
            listing = Listing.objects.get(pk=listing_key)
            reviews = Review.objects.filter(listing=listing)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        except Listing.DoesNotExist:
            return Response({'error': 'Listing not found'}, status=404)

    def post(self, request, listing_key):
        try:
            listing = Listing.objects.get(pk=listing_key)
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, listing=listing)  # Set user and listing
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Listing.DoesNotExist:
            
            return Response({'error': 'Listing not found'}, status=404)
