from django.db import models

# Create your models here.

class schools_master(models.Model):
    district = models.CharField(max_length=30)
    block = models.CharField(max_length=30)
    cluster = models.CharField(max_length=30)
    school_id = models.IntegerField(max_length=30)
    school_name = models.CharField(max_length=100)
    moi = models.CharField(max_length=30)
    math_minimum_or_above_percentage = models.DecimalField(max_digits =10,decimal_places =2)
    kannada_minimum_or_above_percentage = models.DecimalField(max_digits =10,decimal_places =2)
    clas = models.IntegerField(max_length=10)
    total_students = models.IntegerField(max_length=10)
    math_above_average = models.IntegerField(max_length=10)
    math_average = models.IntegerField(max_length=10)
    math_minimum = models.IntegerField(max_length=10)
    math_below_minimum = models.IntegerField(max_length=10)
    kannada_above_average = models.IntegerField(max_length=10)
    kannada_average = models.IntegerField(max_length=10)
    kannada_minimum = models.IntegerField(max_length=10)
    kannada_below_minimum = models.IntegerField(max_length=10)

    class Meta:
        db_table = "schools_master_2011_12"

class district_aggregation(models.Model):
    name = models.CharField(max_length=50)
    clas = models.CharField(max_length =10)
    math_above_average = models.IntegerField(max_length=10)
    math_average = models.IntegerField(max_length=10)
    math_minimum = models.IntegerField(max_length=10)
    math_below_minimum = models.IntegerField(max_length=10)
    kannada_above_average = models.IntegerField(max_length=10)
    kannada_average = models.IntegerField(max_length=10)
    kannada_minimum = models.IntegerField(max_length=10)
    kannada_below_minimum = models.IntegerField(max_length=10)
    total = models.IntegerField(max_length=10)

    class Meta:
        db_table = "district_aggregation_2011_12"

class block_aggregation(models.Model):
    name = models.CharField(max_length=50)
    clas = models.CharField(max_length =10)
    math_above_average = models.IntegerField(max_length=10)
    math_average = models.IntegerField(max_length=10)
    math_minimum = models.IntegerField(max_length=10)
    math_below_minimum = models.IntegerField(max_length=10)
    kannada_above_average = models.IntegerField(max_length=10)
    kannada_average = models.IntegerField(max_length=10)
    kannada_minimum = models.IntegerField(max_length=10)
    kannada_below_minimum = models.IntegerField(max_length=10)
    total = models.IntegerField(max_length=10)

    class Meta:
        db_table = "block_aggregation_2011_12"

class cluster_aggregation(models.Model):
    name = models.CharField(max_length=50)
    clas = models.CharField(max_length =10)
    math_above_average = models.IntegerField(max_length=10)
    math_average = models.IntegerField(max_length=10)
    math_minimum = models.IntegerField(max_length=10)
    math_below_minimum = models.IntegerField(max_length=10)
    kannada_above_average = models.IntegerField(max_length=10)
    kannada_average = models.IntegerField(max_length=10)
    kannada_minimum = models.IntegerField(max_length=10)
    kannada_below_minimum = models.IntegerField(max_length=10)
    total = models.IntegerField(max_length=10)

    class Meta:
        db_table = "cluster_aggregation_2011_12"

class school_aggregation(models.Model):
    name = models.CharField(max_length=50)
    clas = models.CharField(max_length =10)
    math_above_average = models.IntegerField(max_length=10)
    math_average = models.IntegerField(max_length=10)
    math_minimum = models.IntegerField(max_length=10)
    math_below_minimum = models.IntegerField(max_length=10)
    kannada_above_average = models.IntegerField(max_length=10)
    kannada_average = models.IntegerField(max_length=10)
    kannada_minimum = models.IntegerField(max_length=10)
    kannada_below_minimum = models.IntegerField(max_length=10)
    total = models.IntegerField(max_length=10)

    class Meta:
        db_table = "school_aggregation_2011_12"

class state_aggregation(models.Model):
    name = models.CharField(max_length=50)
    clas = models.CharField(max_length =10)
    math_above_average = models.IntegerField(max_length=10)
    math_average = models.IntegerField(max_length=10)
    math_minimum = models.IntegerField(max_length=10)
    math_below_minimum = models.IntegerField(max_length=10)
    kannada_above_average = models.IntegerField(max_length=10)
    kannada_average = models.IntegerField(max_length=10)
    kannada_minimum = models.IntegerField(max_length=10)
    kannada_below_minimum = models.IntegerField(max_length=10)
    total = models.IntegerField(max_length=10)

    class Meta:
        db_table = "state_aggregation_2011_12"
