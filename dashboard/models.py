# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achivement(models.Model):
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'achivement'


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    comment_date = models.CharField(max_length=30)
    created_date = models.DateTimeField()
    post_id = models.BigIntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'
        unique_together = (('id', 'post_id'),)


class Like(models.Model):
    created_at = models.DateTimeField()
    post_id = models.BigIntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'like'
        unique_together = (('id', 'post_id'),)


class Message(models.Model):
    from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Otp(models.Model):
    token = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField()
    status = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp'
        unique_together = (('id', 'user_id'),)


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    like_count = models.PositiveIntegerField()
    comment_count = models.PositiveIntegerField()
    view_count = models.PositiveIntegerField()
    share_count = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=5)
    location = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    user_id = models.PositiveIntegerField()
    thumbnail = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'
        unique_together = (('id', 'user_id'),)


class PostMedia(models.Model):
    post_id = models.BigIntegerField()
    url = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'post_media'
        unique_together = (('id', 'post_id'),)


class User(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    achivement_id = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=250, blank=True, null=True)
    longitude = models.CharField(max_length=250, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    soundcloud = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    range_finder = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.CharField(max_length=250, blank=True, null=True)
    website = models.CharField(max_length=250, blank=True, null=True)
    notification = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class UserBlocked(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    blocked_user_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_blocked'
