# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectorqr', '0002_scanlog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alumno',
            new_name='Paciente',
        ),
        migrations.AlterModelTable(
            name='paciente',
            table='pacientes',
        ),
        migrations.RenameField(
            model_name='scanlog',
            old_name='alumno',
            new_name='paciente',
        ),
        migrations.AlterField(
            model_name='scanlog',
            name='paciente',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='scan_logs',
                to='lectorqr.paciente',
                verbose_name='Paciente Escaneado'
            ),
        ),
    ]
