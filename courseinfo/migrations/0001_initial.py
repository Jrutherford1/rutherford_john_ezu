# Generated by Django 4.1 on 2023-06-13 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("course_number", models.CharField(max_length=20)),
                ("course_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
            fields=[
                ("instructor_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=45)),
                ("last_name", models.CharField(max_length=45)),
                (
                    "disambiguator",
                    models.CharField(blank=True, default="", max_length=45),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Period",
            fields=[
                ("period_id", models.AutoField(primary_key=True, serialize=False)),
                ("period_sequence", models.IntegerField(unique=True)),
                ("period_name", models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("student_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=45)),
                ("last_name", models.CharField(max_length=45)),
                (
                    "disambiguator",
                    models.CharField(blank=True, default="", max_length=45),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Year",
            fields=[
                ("year_id", models.AutoField(primary_key=True, serialize=False)),
                ("year", models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Semester",
            fields=[
                ("semester_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "period",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="semesters",
                        to="courseinfo.period",
                    ),
                ),
                (
                    "year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="semesters",
                        to="courseinfo.year",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                ("section_id", models.AutoField(primary_key=True, serialize=False)),
                ("section_name", models.CharField(max_length=10)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sections",
                        to="courseinfo.course",
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sections",
                        to="courseinfo.instructor",
                    ),
                ),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sections",
                        to="courseinfo.semester",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "registration_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="registrations",
                        to="courseinfo.section",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="registrations",
                        to="courseinfo.student",
                    ),
                ),
            ],
        ),
    ]
