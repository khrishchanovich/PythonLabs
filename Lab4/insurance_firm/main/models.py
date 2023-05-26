from django.db import models

# Create your models here.


class InsuranceType(models.Model):
    title = models.CharField(max_length=100) # ссылка на экземпляр класса
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/insurance_type/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    object = models.ForeignKey('Object', on_delete=models.CASCADE)


class Object(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)


class InsuranceContract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # !!!
    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE) # !!!
    object_insured = models.ForeignKey(Object, on_delete=models.CASCADE) # !!!
    start_date = models.DateField()
    end_date = models.DateField()
    agents = models.ManyToManyField('InsuranceAgent', through='AgentContract')


class InsuranceAgent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    branch = models.OneToOneField('CompanyBranch', on_delete=models.CASCADE)


class CompanyBranch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    agent = models.OneToOneField('InsuranceAgent', on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=10, decimal_places=2)


class AgentContract(models.Model):
    insurance_contract = models.ForeignKey(InsuranceContract, on_delete=models.CASCADE)
    insurance_agent = models.ForeignKey(InsuranceAgent, on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=10, decimal_places=2)