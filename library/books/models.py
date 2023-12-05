from django.db import models

# Create your models here.
class Book(models.Model):
    b_title = models.CharField(max_length=100)
    authour = models.CharField(max_length=100)
    gener=models.CharField(max_length=100)
    isbn =models.CharField(max_length=100)
    available=models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.authour}"


class Customer(models.Model):
    authour= models.ForeignKey(Book,on_delete=models.CASCADE)
    cus_name = models.CharField(max_length=200)
    contact=models.IntegerField()
    membership = models.BooleanField( default=False)
    added_date = models.DateTimeField(auto_now_add=True)
        
        

    def _str_(self):
        return f"{self.cus_name}"


class Borrow(models.Model):
    author= models.ForeignKey(Book,on_delete=models.CASCADE)
    cus_name = models.ForeignKey(Customer,on_delete=models.CASCADE)
    borrow_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(auto_now_add=True)



    def _str_(self):
        return f'{self.author}==>{self.cus_name}==>{self.borrow_date}'
