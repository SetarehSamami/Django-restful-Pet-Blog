from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username,age,email,password):
        if not username:
            raise ValueError('please enter username!')
        if not age:
            raise ValueError('please enter age!')
        if not email:
            raise ValueError('please enter email!')
        
        user=self.model(username=username ,age=age ,email=self.normalize_email(str(email)))
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,username,age,email,password):
        user=self.create_user(username,age,email,password)
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

