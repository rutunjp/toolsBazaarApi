from rest_framework import serializers

from .models import Listing, ListingImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["id", "listing", "image"]


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True)

    class Meta:
        model = Listing
        fields = ('id', 'title', 'price', 'location',
                  'sellerUser', 'images', 'uploaded_images', 'featured')

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        listing = Listing.objects.create(**validated_data)
        for image in uploaded_images:
            newlisting_image = ListingImage.objects.create(
                listing=listing, image=image)
        return listing
