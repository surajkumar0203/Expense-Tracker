from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Transaction(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    chose_option = (('Food','Food'),('Transport','Transport'),('Entertainment','Entertainment'),('Other','Other'))
    expance_name=models.CharField(max_length=100)
    amount=models.FloatField()
    category=models.CharField(choices=chose_option,)

    class Meta:
        ordering=("-amount",)
        db_table="Transaction_Table"
        verbose_name="Transaction_Table"
        
    


