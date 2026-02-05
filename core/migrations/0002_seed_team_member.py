from django.db import migrations


def seed_member(apps, schema_editor):
    TeamMember = apps.get_model('core', 'TeamMember')
    Skill = apps.get_model('core', 'Skill')

    if TeamMember.objects.filter(slug='amira-khan').exists():
        return

    member = TeamMember.objects.create(
        name='Amira Khan',
        slug='amira-khan',
        role='Head of Solar Innovation',
        tagline='Designing climate-positive products with measurable impact.',
        short_bio='Amira leads product strategy across solar intelligence and customer experience.',
        full_bio='''<p>Amira blends engineering, design, and market strategy to launch products that accelerate clean energy adoption.</p><p>She previously led distributed energy initiatives across EMEA and now mentors the Solak innovation guild.</p>''',
        email='amira@solak.energy',
        phone='+1 555 0109',
        linkedin='https://www.linkedin.com/',
        twitter='https://x.com/',
        order=1,
    )

    for idx, (name, pct) in enumerate([
        ('Leadership', 94),
        ('Solar Design', 89),
        ('Data Strategy', 85),
        ('Public Speaking', 91),
    ], start=1):
        Skill.objects.create(member=member, name=name, percentage=pct, order=idx)


def unseed_member(apps, schema_editor):
    TeamMember = apps.get_model('core', 'TeamMember')
    TeamMember.objects.filter(slug='amira-khan').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_member, unseed_member),
    ]
