from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_seed_team_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percentage',
            field=models.PositiveSmallIntegerField(default=75, validators=[MinValueValidator(0), MaxValueValidator(100)]),
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['order', 'id']},
        ),
    ]
