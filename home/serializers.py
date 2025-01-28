from rest_framework import serializers
from .models import Valid_vote,Constituency, District

class ValidVoteSerializer(serializers.ModelSerializer):
    district = serializers.CharField(source='district.name', read_only=True)  # Custom field for district name
    constituency = serializers.CharField(source='constituency.name', read_only=True)  # Custom field for constituency name

    class Meta:
        model = Valid_vote
        fields = [
            'id', 'station_vote', 'advance_vote', 'total_vote', 'percentage', 'win_lose', 
            'candidate', 'party', 'district', 'constituency', 
            'hlutdaw', 'election_year'
        ]  

class ConstituencySerializer(serializers.ModelSerializer):
    district = serializers.CharField(source='district.name', read_only=True)  # Custom field for district name

    class Meta:
        model = Constituency
        fields = ['id', 'name', 'district', 'khayine', 'township', 'file', 'detail_file', 'hlutdaw']  # Specify fields explicitly

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'