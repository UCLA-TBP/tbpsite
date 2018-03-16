# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Class'
        db.create_table(u'tutoring_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('course_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'tutoring', ['Class'])

        # Adding model 'Tutoring'
        db.create_table(u'tutoring_tutoring', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Term'])),
            ('day_1', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('hour_1', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('day_2', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('hour_2', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Profile'])),
            ('best_day', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('best_hour', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('second_best_day', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('second_best_hour', self.gf('django.db.models.fields.CharField')(default='2', max_length=1)),
            ('third_best_day', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('third_best_hour', self.gf('django.db.models.fields.CharField')(default='4', max_length=1)),
            ('week_3', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tutoring.Week3'], unique=True)),
            ('week_4', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tutoring.Week4'], unique=True)),
            ('week_5', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tutoring.Week5'], unique=True)),
            ('week_6', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tutoring.Week6'], unique=True)),
            ('week_7', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tutoring.Week7'], unique=True)),
            ('week_8', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tutoring.Week8'], unique=True)),
            ('week_9', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tutoring.Week9'], unique=True)),
            ('frozen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_tutoring', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_start', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'tutoring', ['Tutoring'])

        # Adding unique constraint on 'Tutoring', fields ['profile', 'term']
        db.create_unique(u'tutoring_tutoring', ['profile_id', 'term_id'])

        # Adding model 'Week3'
        db.create_table(u'tutoring_week3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutees', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_makeup', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tutoring', ['Week3'])

        # Adding M2M table for field classes on 'Week3'
        m2m_table_name = db.shorten_name(u'tutoring_week3_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week3', models.ForeignKey(orm[u'tutoring.week3'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week3_id', 'class_id'])

        # Adding model 'Week4'
        db.create_table(u'tutoring_week4', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutees', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_makeup', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tutoring', ['Week4'])

        # Adding M2M table for field classes on 'Week4'
        m2m_table_name = db.shorten_name(u'tutoring_week4_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week4', models.ForeignKey(orm[u'tutoring.week4'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week4_id', 'class_id'])

        # Adding model 'Week5'
        db.create_table(u'tutoring_week5', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutees', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_makeup', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tutoring', ['Week5'])

        # Adding M2M table for field classes on 'Week5'
        m2m_table_name = db.shorten_name(u'tutoring_week5_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week5', models.ForeignKey(orm[u'tutoring.week5'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week5_id', 'class_id'])

        # Adding model 'Week6'
        db.create_table(u'tutoring_week6', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutees', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_makeup', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tutoring', ['Week6'])

        # Adding M2M table for field classes on 'Week6'
        m2m_table_name = db.shorten_name(u'tutoring_week6_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week6', models.ForeignKey(orm[u'tutoring.week6'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week6_id', 'class_id'])

        # Adding model 'Week7'
        db.create_table(u'tutoring_week7', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutees', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_makeup', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tutoring', ['Week7'])

        # Adding M2M table for field classes on 'Week7'
        m2m_table_name = db.shorten_name(u'tutoring_week7_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week7', models.ForeignKey(orm[u'tutoring.week7'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week7_id', 'class_id'])

        # Adding model 'Week8'
        db.create_table(u'tutoring_week8', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutees', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_makeup', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tutoring', ['Week8'])

        # Adding M2M table for field classes on 'Week8'
        m2m_table_name = db.shorten_name(u'tutoring_week8_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week8', models.ForeignKey(orm[u'tutoring.week8'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week8_id', 'class_id'])

        # Adding model 'Week9'
        db.create_table(u'tutoring_week9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutees', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_makeup', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'tutoring', ['Week9'])

        # Adding M2M table for field classes on 'Week9'
        m2m_table_name = db.shorten_name(u'tutoring_week9_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('week9', models.ForeignKey(orm[u'tutoring.week9'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['week9_id', 'class_id'])

        # Adding model 'ForeignTutoring'
        db.create_table(u'tutoring_foreigntutoring', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Term'])),
            ('day_1', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('hour_1', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('day_2', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('hour_2', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'tutoring', ['ForeignTutoring'])

        # Adding unique constraint on 'ForeignTutoring', fields ['name', 'term']
        db.create_unique(u'tutoring_foreigntutoring', ['name', 'term_id'])

        # Adding M2M table for field classes on 'ForeignTutoring'
        m2m_table_name = db.shorten_name(u'tutoring_foreigntutoring_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('foreigntutoring', models.ForeignKey(orm[u'tutoring.foreigntutoring'], null=False)),
            ('class', models.ForeignKey(orm[u'tutoring.class'], null=False))
        ))
        db.create_unique(m2m_table_name, ['foreigntutoring_id', 'class_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ForeignTutoring', fields ['name', 'term']
        db.delete_unique(u'tutoring_foreigntutoring', ['name', 'term_id'])

        # Removing unique constraint on 'Tutoring', fields ['profile', 'term']
        db.delete_unique(u'tutoring_tutoring', ['profile_id', 'term_id'])

        # Deleting model 'Class'
        db.delete_table(u'tutoring_class')

        # Deleting model 'Tutoring'
        db.delete_table(u'tutoring_tutoring')

        # Deleting model 'Week3'
        db.delete_table(u'tutoring_week3')

        # Removing M2M table for field classes on 'Week3'
        db.delete_table(db.shorten_name(u'tutoring_week3_classes'))

        # Deleting model 'Week4'
        db.delete_table(u'tutoring_week4')

        # Removing M2M table for field classes on 'Week4'
        db.delete_table(db.shorten_name(u'tutoring_week4_classes'))

        # Deleting model 'Week5'
        db.delete_table(u'tutoring_week5')

        # Removing M2M table for field classes on 'Week5'
        db.delete_table(db.shorten_name(u'tutoring_week5_classes'))

        # Deleting model 'Week6'
        db.delete_table(u'tutoring_week6')

        # Removing M2M table for field classes on 'Week6'
        db.delete_table(db.shorten_name(u'tutoring_week6_classes'))

        # Deleting model 'Week7'
        db.delete_table(u'tutoring_week7')

        # Removing M2M table for field classes on 'Week7'
        db.delete_table(db.shorten_name(u'tutoring_week7_classes'))

        # Deleting model 'Week8'
        db.delete_table(u'tutoring_week8')

        # Removing M2M table for field classes on 'Week8'
        db.delete_table(db.shorten_name(u'tutoring_week8_classes'))

        # Deleting model 'Week9'
        db.delete_table(u'tutoring_week9')

        # Removing M2M table for field classes on 'Week9'
        db.delete_table(db.shorten_name(u'tutoring_week9_classes'))

        # Deleting model 'ForeignTutoring'
        db.delete_table(u'tutoring_foreigntutoring')

        # Removing M2M table for field classes on 'ForeignTutoring'
        db.delete_table(db.shorten_name(u'tutoring_foreigntutoring_classes'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.house': {
            'Meta': {'object_name': 'House'},
            'house': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.profile': {
            'Meta': {'ordering': "('position', 'user__last_name', 'user__first_name')", 'object_name': 'Profile'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'graduation_term': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'profile_graduation_term'", 'null': 'True', 'to': u"orm['main.Term']"}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.House']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiation_term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile_initiation_term'", 'to': u"orm['main.Term']"}),
            'major': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'resume_pdf': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resume_word': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'main.term': {
            'Meta': {'ordering': "['-year', '-quarter']", 'unique_together': "(('quarter', 'year'),)", 'object_name': 'Term'},
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tutoring.class': {
            'Meta': {'ordering': "('department', 'course_number')", 'object_name': 'Class'},
            'course_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tutoring.foreigntutoring': {
            'Meta': {'ordering': "('-term', 'name')", 'unique_together': "(('name', 'term'),)", 'object_name': 'ForeignTutoring'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tutoring.Class']", 'symmetrical': 'False'}),
            'day_1': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'day_2': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'hour_1': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'hour_2': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Term']"})
        },
        u'tutoring.tutoring': {
            'Meta': {'ordering': "('-term', 'profile')", 'unique_together': "(('profile', 'term'),)", 'object_name': 'Tutoring'},
            'best_day': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'best_hour': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'day_1': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'day_2': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hour_1': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'hour_2': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_tutoring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_start': ('django.db.models.fields.DateTimeField', [], {}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Profile']"}),
            'second_best_day': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'second_best_hour': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '1'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Term']"}),
            'third_best_day': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'third_best_hour': ('django.db.models.fields.CharField', [], {'default': "'4'", 'max_length': '1'}),
            'week_3': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Week3']", 'unique': 'True'}),
            'week_4': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Week4']", 'unique': 'True'}),
            'week_5': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Week5']", 'unique': 'True'}),
            'week_6': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Week6']", 'unique': 'True'}),
            'week_7': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Week7']", 'unique': 'True'}),
            'week_8': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Week8']", 'unique': 'True'}),
            'week_9': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Week9']", 'unique': 'True'})
        },
        u'tutoring.week3': {
            'Meta': {'ordering': "('tutoring__day_1', 'tutoring__hour_1', 'tutoring__day_2', 'tutoring__hour_2', 'tutoring__profile')", 'object_name': 'Week3'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_makeup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tutees': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'tutoring.week4': {
            'Meta': {'ordering': "('tutoring__day_1', 'tutoring__hour_1', 'tutoring__day_2', 'tutoring__hour_2', 'tutoring__profile')", 'object_name': 'Week4'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_makeup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tutees': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'tutoring.week5': {
            'Meta': {'ordering': "('tutoring__day_1', 'tutoring__hour_1', 'tutoring__day_2', 'tutoring__hour_2', 'tutoring__profile')", 'object_name': 'Week5'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_makeup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tutees': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'tutoring.week6': {
            'Meta': {'ordering': "('tutoring__day_1', 'tutoring__hour_1', 'tutoring__day_2', 'tutoring__hour_2', 'tutoring__profile')", 'object_name': 'Week6'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_makeup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tutees': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'tutoring.week7': {
            'Meta': {'ordering': "('tutoring__day_1', 'tutoring__hour_1', 'tutoring__day_2', 'tutoring__hour_2', 'tutoring__profile')", 'object_name': 'Week7'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_makeup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tutees': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'tutoring.week8': {
            'Meta': {'ordering': "('tutoring__day_1', 'tutoring__hour_1', 'tutoring__day_2', 'tutoring__hour_2', 'tutoring__profile')", 'object_name': 'Week8'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_makeup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tutees': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'tutoring.week9': {
            'Meta': {'ordering': "('tutoring__day_1', 'tutoring__hour_1', 'tutoring__day_2', 'tutoring__hour_2', 'tutoring__profile')", 'object_name': 'Week9'},
            'classes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutoring.Class']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_makeup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tutees': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['tutoring']