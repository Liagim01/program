# Generated by Django 3.2.2 on 2021-12-08 14:07
from django.core.cache import cache
from django.db import migrations


def cleanup(app, schema_editor):
    EventSettingsStore = app.get_model('pretixbase', 'Event_SettingsStore')
    for setting in EventSettingsStore.objects.filter(key='payment_stripe_method_cc'):
        setting.key = 'payment_stripe_method_card'
        cache.delete('hierarkey_{}_{}'.format('event', setting.object_id))
        setting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('stripe', '0003_registeredapplepaydomain'),
    ]

    operations = [
        migrations.RunPython(cleanup, migrations.RunPython.noop)
    ]
