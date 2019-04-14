# Generated by Django 2.2 on 2019-04-14 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('phoneNumber', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=2)),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadTracker.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('notes', models.TextField()),
                ('leadFirstName', models.CharField(max_length=64)),
                ('leadLastName', models.CharField(max_length=64)),
                ('leadPhoneNumber', models.CharField(max_length=32)),
                ('leadEmail', models.EmailField(max_length=254)),
                ('loanAmount', models.IntegerField()),
                ('loanRate', models.FloatField()),
                ('loanCreditScore', models.IntegerField()),
                ('loanMonthlyPayment', models.IntegerField()),
                ('loanTerm', models.IntegerField()),
                ('SCD', models.FloatField()),
                ('oneYearCurr', models.IntegerField()),
                ('currentLender', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadTracker.CustomerCompany')),
                ('loadRateType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadTracker.LoanType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
