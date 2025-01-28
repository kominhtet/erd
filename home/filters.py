import django_filters
from .models import Valid_vote,Constituency, District
from django_filters import rest_framework as filters

class ValidVoteFilter(django_filters.FilterSet):
    district = django_filters.CharFilter(field_name='district__name', lookup_expr='icontains')
    constituency = django_filters.CharFilter(field_name='constituency__name', lookup_expr='icontains')
    election_year = django_filters.CharFilter(field_name='election_year', lookup_expr='icontains')
    hlutdaw = django_filters.CharFilter(field_name='hlutdaw', lookup_expr='icontains')
    party = django_filters.CharFilter(field_name='party', lookup_expr='icontains')
    
    class Meta:
        model = Valid_vote
        fields = ['district', 'constituency', 'election_year', 'hlutdaw', 'party']

class ConstituencyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    district = filters.NumberFilter(field_name="district__id", lookup_expr="exact")
    hlutdaw = django_filters.CharFilter(field_name='hlutdaw', lookup_expr='icontains')
    class Meta:
        model = Constituency
        fields = ['name', 'hlutdaw']
    
class DistrictFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = District
        fields = ['name']