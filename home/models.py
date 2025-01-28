from django.db import models
import hashlib

def hash_filename(instance, filename):
    hashed_name = hashlib.sha256(filename.encode('utf-8')).hexdigest()
    file_extension = filename[filename.rfind('.'):]
    return f"{hashed_name}{file_extension}"
    
class Party(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='party_logos/', blank=True, null=True)
    # Add any other fields you need for the Party model
    def __str__(self):
        return self.name

#တိုင်းဒေသကြီး/ပြည်နယ်
class District(models.Model):  
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='district/', blank=True, null=True)
    def __str__(self):
        return self.name

#ခရိုင်
class Khayine(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

class Township(models.Model):
    name = models.CharField(max_length=200)
    khayine = models.ForeignKey(Khayine, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

class Constituency(models.Model):
    name = models.CharField(max_length=200,unique=True)  
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    khayine = models.ForeignKey(Khayine, on_delete=models.CASCADE, blank=True, null=True)
    township = models.ForeignKey(Township, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='constituency/', blank=True, null=True)
    detail_file = models.FileField(upload_to='constituency/details', blank=True, null=True)
    hlutdaw = models.CharField(max_length=200, blank=True, null=True)
  
    def __str__(self):
        return f"{self.name} -> {self.hlutdaw}{self.district}"
    
class Numberofvoters1(models.Model):
    can_vote = models.IntegerField(blank=True, null=True)
    station_vote = models.IntegerField(blank=True, null=True)  
    advance_vote = models.IntegerField(blank=True, null=True)  
    total_vote = models.IntegerField(blank=True, null=True)  
    constituency = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    election_year = models.IntegerField(blank=True, null=True)
    
class Valid_vote(models.Model):
    station_vote = models.IntegerField(blank=True, null=True)
    advance_vote = models.IntegerField(blank=True, null=True)
    total_vote = models.IntegerField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    candidate = models.CharField(max_length=200, blank=True, null=True)
    party = models.CharField(max_length=200, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)  # Ensure this exists
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    hlutdaw = models.CharField(max_length=200, blank=True, null=True)
    election_year = models.IntegerField(blank=True, null=True)
    win_lose = models.BooleanField(blank=True, null=True)

    def __str__(self):
        
        return f"{self.district} -> {self.hlutdaw} ->{self.election_year} ->{self.constituency.name}"