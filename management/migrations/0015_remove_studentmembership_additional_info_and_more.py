# Generated by Django 4.1 on 2024-02-02 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0014_remove_generalmembership_educational_document_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentmembership",
            name="additional_info",
        ),
        migrations.AddField(
            model_name="studentmembership",
            name="nationaldocument",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_membership",
                to="management.nationaldocumment",
            ),
        ),
    ]
