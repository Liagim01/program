# Generated by Django 4.2.4 on 2023-09-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pretixbase", "0245_discount_benefit_products"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="logentry",
            new_name="pretixbase__datetim_b1fe5a_idx",
            old_fields=("datetime", "id"),
        ),
        migrations.RenameIndex(
            model_name="order",
            new_name="pretixbase__datetim_66aff0_idx",
            old_fields=("datetime", "id"),
        ),
        migrations.RenameIndex(
            model_name="order",
            new_name="pretixbase__last_mo_4ebf8b_idx",
            old_fields=("last_modified", "id"),
        ),
        migrations.RenameIndex(
            model_name="reusablemedium",
            new_name="pretixbase__updated_093277_idx",
            old_fields=("updated", "id"),
        ),
        migrations.RenameIndex(
            model_name="transaction",
            new_name="pretixbase__datetim_b20405_idx",
            old_fields=("datetime", "id"),
        ),
        migrations.AlterField(
            model_name="attendeeprofile",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="blockedticketsecret",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="cachedcombinedticket",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="cachedticket",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="cancellationrequest",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="cartposition",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="checkin",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="checkinlist",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="locale",
            field=models.CharField(default="de", max_length=50),
        ),
        migrations.AlterField(
            model_name="device",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="discount",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="event_settingsstore",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="eventfooterlink",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="eventmetaproperty",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="eventmetavalue",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="exchangerate",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="gate",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="giftcard",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="giftcardacceptance",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="giftcardtransaction",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="globalsettingsobject_settingsstore",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="invoiceaddress",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="invoiceline",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="itemaddon",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="itembundle",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="itemcategory",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="itemmetaproperty",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="itemmetavalue",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="itemvariation",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="itemvariationmetavalue",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="logentry",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="mediumkeyset",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="notificationsetting",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="orderfee",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="orderpayment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="orderposition",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="orderrefund",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="organizer",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="organizer_settingsstore",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="organizerfooterlink",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="questionanswer",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="questionoption",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="quota",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="revokedticketsecret",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="seat",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="seatcategorymapping",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="seatingplan",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="staffsession",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="staffsessionauditlog",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="subevent",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="subeventitem",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="subeventitemvariation",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="subeventmetavalue",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="taxrule",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="teamapitoken",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="teaminvite",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="u2fdevice",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="locale",
            field=models.CharField(default="de", max_length=50),
        ),
        migrations.AlterField(
            model_name="voucher",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="waitinglistentry",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="webauthndevice",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
    ]
