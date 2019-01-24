# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'main_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'main', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'main_link')


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
        u'main.activemember': {
            'Meta': {'ordering': "('term', 'profile__user__last_name', 'profile__user__first_name')", 'unique_together': "(('profile', 'term'),)", 'object_name': 'ActiveMember'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'event_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['main.Requirement']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'peer_teaching': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.PeerTeaching']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Profile']"}),
            'requirement_choice': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'requirement_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Term']"}),
            'tutoring': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Tutoring']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'main.candidate': {
            'Meta': {'ordering': "('term', 'profile__user__last_name', 'profile__user__first_name')", 'object_name': 'Candidate'},
            'bent_polish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'candidate_meet_and_greet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'candidate_quiz': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'candidate_sorting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'community_service': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'community_service_proof': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'engineering_futures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'event_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['main.Requirement']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiation_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'peer_teaching': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.PeerTeaching']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'professor_interview': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'professor_interview_on_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Profile']", 'unique': 'True'}),
            'quiz_first_try': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resume_on_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '2'}),
            'signature_book': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tbp_event': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Term']"}),
            'tutoring': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Tutoring']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'main.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'chapter': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'graduation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'main.house': {
            'Meta': {'object_name': 'House'},
            'house': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.housepoints': {
            'Meta': {'ordering': "('-term', 'house')", 'unique_together': "(('house', 'term'),)", 'object_name': 'HousePoints'},
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.House']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'professor_interview_and_resume': ('django.db.models.fields.CharField', [], {'default': "'4'", 'max_length': '1'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Term']"})
        },
        u'main.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        },
        u'main.officer': {
            'Meta': {'ordering': "('rank',)", 'object_name': 'Officer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail_alias': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Profile']", 'symmetrical': 'False'}),
            'rank': ('django.db.models.fields.IntegerField', [], {})
        },
        u'main.peerteaching': {
            'Meta': {'object_name': 'PeerTeaching'},
            'academic_outreach_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'emcc_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Profile']", 'null': 'True', 'blank': 'True'}),
            'requirement_choice': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Term']", 'null': 'True', 'blank': 'True'}),
            'tutoring': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tutoring.Tutoring']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
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
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'main.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'event_hours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'requirement_choice': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Term']"})
        },
        u'main.reviewsheet': {
            'Meta': {'ordering': "['course']", 'object_name': 'ReviewSheet'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutoring.Class']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reviewSheetFile': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True'})
        },
        u'main.settings': {
            'Meta': {'object_name': 'Settings'},
            'display_all_terms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_tutoring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eligibility_list': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'signup_term': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'signup'", 'null': 'True', 'to': u"orm['main.Term']"}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current'", 'null': 'True', 'to': u"orm['main.Term']"})
        },
        u'main.term': {
            'Meta': {'ordering': "['-year', '-quarter']", 'unique_together': "(('quarter', 'year'),)", 'object_name': 'Term'},
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'main.test_upload': {
            'Meta': {'ordering': "['course', 'professor', 'test_type']", 'object_name': 'Test_Upload'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutoring.Class']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin_term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'test_origin_term'", 'null': 'True', 'to': u"orm['main.Term']"}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Profile']", 'null': 'True', 'blank': 'True'}),
            'test_type': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '10', 'blank': 'True'}),
            'test_upload': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True'})
        },
        u'tutoring.class': {
            'Meta': {'ordering': "('department', 'course_number')", 'object_name': 'Class'},
            'course_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tutoring.tutoring': {
            'Meta': {'ordering': "('-term', 'profile')", 'unique_together': "(('profile', 'term'),)", 'object_name': 'Tutoring'},
            'best_day': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'best_hour': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'day_1': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'day_2': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hour_1': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'hour_2': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_tutoring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2019, 1, 11, 0, 0)'}),
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

    complete_apps = ['main']