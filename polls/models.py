from django.db import models
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Eleitor(models.Model):
    FRESHMAN = 'Inativo'
    SOPHOMORE = 'Ativo'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Inativo'),
        (SOPHOMORE, 'Ativo'),
    ]
    nome = models.CharField(verbose_name="Nome", max_length=100, null=True, blank=True)
    sexo = models.CharField(verbose_name="Sexo", max_length=100,null=True, blank=True)
    bairro = models.CharField(verbose_name="Bairro",max_length=100, null=True, blank=True)
    codigo = models.AutoField(verbose_name="Código", primary_key=True)
    data_de_nascimento = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
    quarteirao = models.CharField(verbose_name="Quarteirão", max_length=100, null=True, blank=True)
    numero_de_casa = models.CharField(verbose_name="Nr Casa", max_length=100, null=True, blank=True)
    bilhete_de_identidade = models.CharField(verbose_name="BI", max_length=100, null=True, blank=True)
    # hora_de_voto = models.DateTimeField(verbose_name="Hora de Voto", null=True, blank=True, auto_now=True) 
    # hora_de_voto=models.AutoField(default=timezone.now)
    estado = models.CharField(verbose_name="Estado do Voto", max_length=100, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN)

    def __str__(self):
        return "Nome Eleitor: "+self.nome+".  /// Codigo do Eleitor: 0"+str(self.codigo)

