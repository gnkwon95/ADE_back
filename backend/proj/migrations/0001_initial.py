# Generated by Django 3.0.8 on 2020-08-03 06:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_company', models.CharField(max_length=20)),
                ('current_job', models.CharField(max_length=20)),
                ('work_period_from', models.DateField()),
                ('work_period_to', models.DateField(blank=True, null=True)),
                ('PR', models.TextField()),
                ('real_name', models.CharField(max_length=20)),
                ('phone_number', models.BigIntegerField()),
                ('bank', models.CharField(default='', max_length=20)),
                ('account_num', models.BigIntegerField()),
                ('account_email', models.CharField(default='', max_length=20)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_uid', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('user_id', models.CharField(max_length=20)),
                ('credit', models.PositiveSmallIntegerField(default=0)),
                ('credit_used', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('granted_by', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='proj.User')),
                ('granted_to', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='granted_to', to='proj.MentorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MentorProfileWorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workexperience', models.CharField(max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.MentorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MentorProfileExtracurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extracurricular', models.CharField(max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.MentorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MentorProfileCertificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.MentorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MentorProfileAppliedCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliedcompany', models.CharField(max_length=20)),
                ('appliedcompanystage', models.CharField(default='최종합', max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.MentorProfile')),
            ],
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id_mentor_profile', to='proj.User'),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='voter',
            field=models.ManyToManyField(related_name='voter_profile', to='proj.User'),
        ),
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_date', models.DateField(verbose_name='date published')),
                ('meeting_date', models.DateField()),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='connection_mentee', to='proj.User')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='connection_mentor', to='proj.MentorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.MentorProfile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id_comment', to='proj.User')),
                ('voter', models.ManyToManyField(blank=True, related_name='voter_comment', to='proj.User')),
            ],
        ),
    ]
