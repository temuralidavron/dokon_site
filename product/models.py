from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=500)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=500)
    context = models.TextField()
    image = models.ImageField(upload_to='product/')
    price = models.IntegerField()
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
