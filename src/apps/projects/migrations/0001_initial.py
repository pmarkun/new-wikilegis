# Generated by Django 2.2 on 2019-05-30 13:02

import colorful.fields
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
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(default='Untitled Document', max_length=200, verbose_name='title')),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(default='Document description', verbose_name='description')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='number')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='year')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author_type', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Document Author',
                'verbose_name_plural': 'Document Authors',
            },
        ),
        migrations.CreateModel(
            name='DocumentResponsible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cd_id', models.PositiveIntegerField(default=0, verbose_name='CD ID')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='image url')),
                ('party_initials', models.CharField(blank=True, max_length=250, null=True, verbose_name='party initials')),
                ('uf', models.CharField(blank=True, max_length=250, null=True, verbose_name='uf')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=250, null=True, verbose_name='phone')),
            ],
            options={
                'verbose_name': 'Document Responsible',
                'verbose_name_plural': 'Document Responsibles',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('initials', models.CharField(max_length=200, verbose_name='initials')),
            ],
            options={
                'verbose_name': 'document type',
                'verbose_name_plural': 'document types',
            },
        ),
        migrations.CreateModel(
            name='DocumentVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('number', models.PositiveIntegerField(default=0)),
                ('auto_save', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='projects.Document', verbose_name='document')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='projects.DocumentVersion', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'document version',
                'verbose_name_plural': 'document versions',
                'ordering': ['-created'],
                'unique_together': {('document', 'number')},
            },
        ),
        migrations.CreateModel(
            name='ExcerptType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='excerpt type')),
                ('slug', models.SlugField(max_length=200)),
                ('align_center', models.BooleanField(default=False, verbose_name='align center')),
            ],
            options={
                'verbose_name': 'excerpt type',
                'verbose_name_plural': 'excerpt types',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=200)),
                ('color', colorful.fields.RGBColorField()),
                ('icon', models.FileField(blank=True, null=True, upload_to='icons/', verbose_name='icon')),
            ],
            options={
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
            },
        ),
        migrations.CreateModel(
            name='Excerpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('number', models.PositiveIntegerField(blank=True, null=True, verbose_name='number')),
                ('content', models.TextField(verbose_name='content')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excerpts', to='projects.Document', verbose_name='document')),
                ('excerpt_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.ExcerptType', verbose_name='excerpt type')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excerpts', to='projects.DocumentVersion', verbose_name='version')),
            ],
            options={
                'verbose_name': 'excerpt',
                'verbose_name_plural': 'excerpts',
                'ordering': ('-version', 'order', 'id'),
            },
        ),
        migrations.CreateModel(
            name='DocumentVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('video_id', models.CharField(max_length=200, verbose_name='youtube id')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='projects.Document', verbose_name='document')),
            ],
            options={
                'verbose_name': 'document video',
                'verbose_name_plural': 'document videos',
            },
        ),
        migrations.CreateModel(
            name='DocumentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_id', models.PositiveIntegerField(default=0, verbose_name='CD ID')),
                ('abridgement', models.TextField(blank=True, null=True, verbose_name='abridgement')),
                ('status', models.CharField(blank=True, max_length=250, null=True, verbose_name='status')),
                ('legislative_body', models.CharField(blank=True, max_length=250, null=True, verbose_name='legislative body')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='keywords')),
                ('authors', models.ManyToManyField(blank=True, related_name='documents', to='projects.DocumentAuthor')),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='projects.Document', verbose_name='document')),
            ],
            options={
                'verbose_name': 'Document Information',
                'verbose_name_plural': 'Document Informations',
            },
        ),
        migrations.CreateModel(
            name='DocumentAuthorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_id', models.PositiveIntegerField(default=0, verbose_name='CD ID')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='image url')),
                ('party_initials', models.CharField(blank=True, max_length=250, null=True, verbose_name='party initials')),
                ('uf', models.CharField(blank=True, max_length=250, null=True, verbose_name='uf')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='projects.DocumentAuthor', verbose_name='author')),
            ],
            options={
                'verbose_name': 'Author Information',
                'verbose_name_plural': 'Authors Informations',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.DocumentType', verbose_name='document type'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='document',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents', to='projects.DocumentResponsible', verbose_name='responsible'),
        ),
        migrations.AddField(
            model_name='document',
            name='themes',
            field=models.ManyToManyField(to='projects.Theme', verbose_name='themes'),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together={('document_type', 'number', 'year')},
        ),
    ]
