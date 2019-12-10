# Generated by Django 2.0 on 2019-08-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DevcieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, max_length=40, null=True)),
                ('device_ip', models.CharField(blank=True, max_length=30, null=True)),
                ('device_port', models.CharField(blank=True, max_length=20, null=True)),
                ('device_type', models.CharField(blank=True, max_length=20, null=True)),
                ('commu_type', models.CharField(blank=True, max_length=30, null=True)),
                ('commu_url', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'devcie_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OpcAddressTb',
            fields=[
                ('serial_nbr', models.AutoField(primary_key=True, serialize=False)),
                ('plc_no', models.CharField(blank=True, max_length=10, null=True)),
                ('plc_node', models.CharField(blank=True, max_length=20, null=True)),
                ('route_addr', models.CharField(blank=True, db_column='route_Addr', max_length=50, null=True)),
                ('readflag_addr', models.CharField(blank=True, db_column='readflag_Addr', max_length=50, null=True)),
                ('device_zone', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'opc_address_tb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rizhibiao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rizhileixing', models.CharField(blank=True, max_length=20, null=True)),
                ('rizhiguanjianzi', models.CharField(blank=True, max_length=20, null=True)),
                ('rizhibianhao', models.CharField(blank=True, max_length=20, null=True)),
                ('rizhimingxi', models.CharField(blank=True, max_length=20, null=True)),
                ('datatime', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rizhibiao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RouteNode',
            fields=[
                ('serialno', models.CharField(db_column='serialNo', max_length=20, primary_key=True, serialize=False)),
                ('sourcenode', models.CharField(blank=True, db_column='sourceNode', max_length=50, null=True)),
                ('destinnode', models.CharField(blank=True, db_column='destinNode', max_length=20, null=True)),
            ],
            options={
                'db_table': 'route_node',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SortScanNode',
            fields=[
                ('serial_nbr', models.AutoField(primary_key=True, serialize=False)),
                ('device_name', models.CharField(blank=True, max_length=50, null=True)),
                ('device_zone', models.CharField(blank=True, max_length=50, null=True)),
                ('scan_node', models.CharField(blank=True, max_length=40, null=True)),
                ('scan_ip', models.CharField(blank=True, max_length=40, null=True)),
                ('scan_port', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'sort_scan_node',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ssx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sbid', models.CharField(blank=True, max_length=255, null=True)),
                ('sbmc', models.CharField(blank=True, max_length=255, null=True)),
                ('zt', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'ssx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('usersex', models.CharField(blank=True, max_length=255, null=True)),
                ('userage', models.CharField(blank=True, max_length=255, null=True)),
                ('authority', models.CharField(blank=True, max_length=20, null=True)),
                ('creationtimes', models.CharField(blank=True, max_length=20, null=True)),
                ('updatetimes', models.CharField(blank=True, max_length=20, null=True)),
                ('states', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
