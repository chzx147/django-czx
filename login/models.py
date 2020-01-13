from django.db import models


# Create your models here.
class user ( models.Model ):
    u_name = models.CharField ( max_length=10 )  # 保存用户名
    u_password = models.CharField ( max_length=255 )  # 保存密码

    class Meta:
        db_table = 'user'