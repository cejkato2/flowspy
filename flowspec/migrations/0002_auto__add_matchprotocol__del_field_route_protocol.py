# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'MatchProtocol'
        db.create_table(u'match_protocol', (
            ('protocol', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('flowspec', ['MatchProtocol'])

        # Deleting field 'Route.protocol'
        db.delete_column(u'route', 'protocol')

        # Adding M2M table for field protocol on 'Route'
        db.create_table(u'route_protocol', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('route', models.ForeignKey(orm['flowspec.route'], null=False)),
            ('matchprotocol', models.ForeignKey(orm['flowspec.matchprotocol'], null=False))
        ))
        db.create_unique(u'route_protocol', ['route_id', 'matchprotocol_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'MatchProtocol'
        db.delete_table(u'match_protocol')

        # Adding field 'Route.protocol'
        db.add_column(u'route', 'protocol', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True), keep_default=False)

        # Removing M2M table for field protocol on 'Route'
        db.delete_table('route_protocol')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'flowspec.matchdscp': {
            'Meta': {'object_name': 'MatchDscp', 'db_table': "u'match_dscp'"},
            'dscp': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flowspec.matchport': {
            'Meta': {'object_name': 'MatchPort', 'db_table': "u'match_port'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'port': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'})
        },
        'flowspec.matchprotocol': {
            'Meta': {'object_name': 'MatchProtocol', 'db_table': "u'match_protocol'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'})
        },
        'flowspec.route': {
            'Meta': {'object_name': 'Route', 'db_table': "u'route'"},
            'applier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'destinationport': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'matchDestinationPort'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['flowspec.MatchPort']"}),
            'dscp': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['flowspec.MatchDscp']", 'null': 'True', 'blank': 'True'}),
            'expires': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 2, 22)'}),
            'filed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fragmenttype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'icmpcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'icmptype': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'packetlength': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'port': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'matchPort'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['flowspec.MatchPort']"}),
            'protocol': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['flowspec.MatchProtocol']", 'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'sourceport': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'matchSourcePort'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['flowspec.MatchPort']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tcpflag': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'then': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['flowspec.ThenAction']", 'symmetrical': 'False'})
        },
        'flowspec.thenaction': {
            'Meta': {'unique_together': "(('action', 'action_value'),)", 'object_name': 'ThenAction', 'db_table': "u'then_action'"},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'action_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['flowspec']
