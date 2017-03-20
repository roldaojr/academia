from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from .percent_gordura import formulas

metodos_gordura = {f.__name__: f for f in formulas}
metodos_gordura_nomes = {f.__name__: f.nome for f in formulas}


def refazer_dia():
    return timezone.now() + timedelta(days=90)


class UsuarioManager(BaseUserManager):
    def create_user(self, login, password=None):
        ''' Cria e salva usuário a partir de usuario e senha '''
        if not login:
            raise ValueError('Usuário deve ter endereço de e-mail')

        user = self.model(login=login)
        user.tipo = 2
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        ''' Cria e salva super usuário a partir de usuario e senha '''
        user = self.create_user(login, password=password)
        user.tipo = 3
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(null=True)
    sexo = models.IntegerField(choices=((1, 'Masculino'), (2, 'Feminino')), null=True)
    login = models.CharField(max_length=10, unique=True)
    tipo = models.IntegerField(default=1, choices=((3, 'Administrador'), (1, 'Aluno'), (2, 'Treinador')))

    objects = UsuarioManager()
    USERNAME_FIELD = 'login'


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField()


class AvaliacaoFisica(models.Model):
    data_realizada = models.DateField(default=timezone.now)
    data_refazer = models.DateField(default=refazer_dia)
    pessoa = models.ForeignKey(Usuario, editable=False)


class PerguntaAnamnese(models.Model):
    texto = models.CharField(max_length=500)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.texto


class RespostaAnamnese(models.Model):
    avaliacaofisica = models.ForeignKey(AvaliacaoFisica, editable=False,
                                        related_name='respostas_anamnese')
    pergunta = models.ForeignKey(PerguntaAnamnese)
    texto = models.CharField(blank=True, null=True, max_length=500, verbose_name='resposta')
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.texto


class Dobra(models.Model):
    metodo = models.CharField(max_length=50, choices=metodos_gordura_nomes.items())
    resultado = models.FloatField(editable=False, default=0)
    tricipes = models.FloatField(null=True, blank=True)
    bicipes = models.FloatField(null=True, blank=True)
    subescapular = models.FloatField(null=True, blank=True)
    suprailiaca = models.FloatField(null=True, blank=True)
    toracica = models.FloatField(null=True, blank=True)
    axilarmedia = models.FloatField(null=True, blank=True)
    abdominal = models.FloatField(null=True, blank=True)
    coxa = models.FloatField(null=True, blank=True)
    panturrilhamedia = models.FloatField(null=True, blank=True)
    avaliacaofisica = models.OneToOneField(AvaliacaoFisica, editable=False)

    def save(self, *args, **kwargs):
        self.resultado = metodos_gordura[self.metodo](self, self.avaliacaofisica.pessoa)
        return super(Dobra, self).save(*args, **kwargs)

class Perimetria(models.Model):
    altura = models.FloatField(null=True)
    peso = models.FloatField(null=True)
    pescoco = models.FloatField(null=True)
    torax = models.FloatField(null=True)
    cintura = models.FloatField(null=True)
    abdome = models.FloatField(null=True)
    quadril = models.FloatField(null=True)
    bicipesdireito = models.FloatField(null=True)
    bicipesesquedo = models.FloatField(null=True)
    tricipesdireito = models.FloatField(null=True)
    tricipesesquerdo = models.FloatField(null=True)
    antebracodireito = models.FloatField(null=True)
    antebracoesquerdo = models.FloatField(null=True)
    coxadireita = models.FloatField(null=True)
    coxaesquerda = models.FloatField(null=True)
    panturrilhadireta = models.FloatField(null=True)
    panturrilhaesquerda = models.FloatField(null=True)
    avaliacaofisica = models.OneToOneField(AvaliacaoFisica, editable=False)


class Treino(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField(default=timezone.now)
    data_fim = models.DateField(default=refazer_dia)
    pessoa = models.ForeignKey(Usuario)


dias_da_semana = (
    (0, 'Domingo'), (1, 'Segunda-feira'), (2, 'Terça-feira'),
    (3, 'Quarta-feira'), (4, 'Quinta-feira'), (5, 'Sexta-feira'), (6, 'Sábado')
)


class Serie(models.Model):
    quantidade = models.IntegerField()
    repeticao = models.IntegerField(verbose_name='Repetição')
    dia = models.IntegerField(choices=dias_da_semana)
    exercicio = models.ForeignKey(Exercicio)
    treino = models.ForeignKey(Treino)
