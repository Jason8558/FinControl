from django.db import models
import datetime
from django.contrib.auth.models import User


class money_type(models.Model):
    name = models.CharField(verbose_name = 'Наименование', max_length=40, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Вид денежных средств'
    
    def __str__(self):
        return self.name


class move_type(models.Model):
    name = models.CharField(verbose_name = 'Наименование', max_length=40, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Вид движения'
    
    def __str__(self):
        return self.name
    

class category(models.Model):
    name = models.CharField(verbose_name = 'Наименование', max_length=250, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория расходов'
    
    def __str__(self):
        return self.name
    
class transaction(models.Model):
    event_date  = models.DateTimeField(verbose_name='Дата', default=datetime.datetime.now, blank=False, null=False)
    summa       = models.FloatField(verbose_name='Сумма операции', null=False, blank=False)
    cashback    = models.FloatField(verbose_name='Кэшбек', null=True, blank=True)
    category    = models.ForeignKey('category', on_delete=models.CASCADE, verbose_name='Категория расходов')
    movetype    = models.ForeignKey('move_type', on_delete=models.CASCADE, verbose_name='Вид движения')
    moneytype   = models.ForeignKey('money_type', on_delete=models.CASCADE, verbose_name='Вид д/с')
    description = models.CharField(verbose_name='Описание', max_length=256, null=True, blank=True)
    owner       = models.ForeignKey('auth.user', on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Транзакция'
        ordering = ['event_date', 'owner']
    
    def __str__(self):
        return 'Транзакция от ' + str(self.event_date)
    
class current_total(models.Model):
    period      = models.DateTimeField(verbose_name='Период', blank=False, null=False)
    value       = models.FloatField(verbose_name='Сумма', null=False, blank=True)
    moneytype   = models.ForeignKey('money_type', on_delete=models.CASCADE, verbose_name='Вид д/с')
    owner       = models.ForeignKey('auth.user', on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Текущий остаток'
        ordering = ['-period', 'moneytype', 'owner']
    
    def __str__(self):
        return 'Остаток по: ' + str(self.moneytype) + ' на ' + str(self.period)