from django.contrib import admin
from .models import Party, District, Khayine, Township, Constituency, Numberofvoters1, Valid_vote
# Register your models here.
admin.site.register(Party)
admin.site.register(District)
admin.site.register(Khayine)
admin.site.register(Township)
admin.site.register(Constituency)
admin.site.register(Numberofvoters1)
admin.site.register(Valid_vote)