# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gabriel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gabriel.proto',
  package='gabriel',
  syntax='proto3',
  serialized_pb=_b('\n\rgabriel.proto\x12\x07gabriel\x1a\x19google/protobuf/any.proto\"\xd5\x01\n\nFromClient\x12\x10\n\x08\x66rame_id\x18\x01 \x01(\x04\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.gabriel.FromClient.Type\x12\x13\n\x0b\x65ngine_name\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12+\n\rengine_fields\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\":\n\x04Type\x12\t\n\x05IMAGE\x10\x00\x12\t\n\x05VIDEO\x10\x01\x12\t\n\x05\x41UDIO\x10\x02\x12\x11\n\rACCELEROMETER\x10\x03\"D\n\x0c\x45ngineServer\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x18\n\x10serialized_proto\x18\x03 \x01(\x0c\"\xc4\x03\n\nFromServer\x12\x10\n\x08\x66rame_id\x18\x01 \x01(\x04\x12*\n\x06status\x18\x02 \x01(\x0e\x32\x1a.gabriel.FromServer.Status\x12+\n\x07results\x18\x03 \x03(\x0b\x32\x1a.gabriel.FromServer.Result\x1a\xab\x01\n\x06Result\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.gabriel.FromServer.Result.ResultType\x12\x13\n\x0b\x65ngine_name\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"F\n\nResultType\x12\t\n\x05IMAGE\x10\x00\x12\t\n\x05VIDEO\x10\x01\x12\t\n\x05\x41UDIO\x10\x02\x12\x08\n\x04TEXT\x10\x03\x12\r\n\tANIMATION\x10\x04\"\x9c\x01\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x13\n\x0fWELCOME_MESSAGE\x10\x01\x12\x15\n\x11UNSPECIFIED_ERROR\x10\x02\x12\x16\n\x12WRONG_INPUT_FORMAT\x10\x03\x12\"\n\x1eREQUESTED_ENGINE_NOT_AVAILABLE\x10\x04\x12\r\n\tNO_TOKENS\x10\x05\x12\x0e\n\nQUEUE_FULL\x10\x06\x42$\n\x1a\x65\x64u.cmu.cs.gabriel.networkB\x06Protosb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FROMCLIENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='gabriel.FromClient.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCELEROMETER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=209,
  serialized_end=267,
)
_sym_db.RegisterEnumDescriptor(_FROMCLIENT_TYPE)

_FROMSERVER_RESULT_RESULTTYPE = _descriptor.EnumDescriptor(
  name='ResultType',
  full_name='gabriel.FromServer.Result.ResultType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANIMATION', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=563,
  serialized_end=633,
)
_sym_db.RegisterEnumDescriptor(_FROMSERVER_RESULT_RESULTTYPE)

_FROMSERVER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='gabriel.FromServer.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WELCOME_MESSAGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_INPUT_FORMAT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUESTED_ENGINE_NOT_AVAILABLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_TOKENS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUE_FULL', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=636,
  serialized_end=792,
)
_sym_db.RegisterEnumDescriptor(_FROMSERVER_STATUS)


_FROMCLIENT = _descriptor.Descriptor(
  name='FromClient',
  full_name='gabriel.FromClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='gabriel.FromClient.frame_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='gabriel.FromClient.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='engine_name', full_name='gabriel.FromClient.engine_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='gabriel.FromClient.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='engine_fields', full_name='gabriel.FromClient.engine_fields', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FROMCLIENT_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=267,
)


_ENGINESERVER = _descriptor.Descriptor(
  name='EngineServer',
  full_name='gabriel.EngineServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='gabriel.EngineServer.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='gabriel.EngineServer.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialized_proto', full_name='gabriel.EngineServer.serialized_proto', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=337,
)


_FROMSERVER_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='gabriel.FromServer.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='gabriel.FromServer.Result.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='engine_name', full_name='gabriel.FromServer.Result.engine_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='gabriel.FromServer.Result.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FROMSERVER_RESULT_RESULTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=462,
  serialized_end=633,
)

_FROMSERVER = _descriptor.Descriptor(
  name='FromServer',
  full_name='gabriel.FromServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='gabriel.FromServer.frame_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='gabriel.FromServer.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='results', full_name='gabriel.FromServer.results', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FROMSERVER_RESULT, ],
  enum_types=[
    _FROMSERVER_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=792,
)

_FROMCLIENT.fields_by_name['type'].enum_type = _FROMCLIENT_TYPE
_FROMCLIENT.fields_by_name['engine_fields'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FROMCLIENT_TYPE.containing_type = _FROMCLIENT
_FROMSERVER_RESULT.fields_by_name['type'].enum_type = _FROMSERVER_RESULT_RESULTTYPE
_FROMSERVER_RESULT.containing_type = _FROMSERVER
_FROMSERVER_RESULT_RESULTTYPE.containing_type = _FROMSERVER_RESULT
_FROMSERVER.fields_by_name['status'].enum_type = _FROMSERVER_STATUS
_FROMSERVER.fields_by_name['results'].message_type = _FROMSERVER_RESULT
_FROMSERVER_STATUS.containing_type = _FROMSERVER
DESCRIPTOR.message_types_by_name['FromClient'] = _FROMCLIENT
DESCRIPTOR.message_types_by_name['EngineServer'] = _ENGINESERVER
DESCRIPTOR.message_types_by_name['FromServer'] = _FROMSERVER

FromClient = _reflection.GeneratedProtocolMessageType('FromClient', (_message.Message,), dict(
  DESCRIPTOR = _FROMCLIENT,
  __module__ = 'gabriel_pb2'
  # @@protoc_insertion_point(class_scope:gabriel.FromClient)
  ))
_sym_db.RegisterMessage(FromClient)

EngineServer = _reflection.GeneratedProtocolMessageType('EngineServer', (_message.Message,), dict(
  DESCRIPTOR = _ENGINESERVER,
  __module__ = 'gabriel_pb2'
  # @@protoc_insertion_point(class_scope:gabriel.EngineServer)
  ))
_sym_db.RegisterMessage(EngineServer)

FromServer = _reflection.GeneratedProtocolMessageType('FromServer', (_message.Message,), dict(

  Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
    DESCRIPTOR = _FROMSERVER_RESULT,
    __module__ = 'gabriel_pb2'
    # @@protoc_insertion_point(class_scope:gabriel.FromServer.Result)
    ))
  ,
  DESCRIPTOR = _FROMSERVER,
  __module__ = 'gabriel_pb2'
  # @@protoc_insertion_point(class_scope:gabriel.FromServer)
  ))
_sym_db.RegisterMessage(FromServer)
_sym_db.RegisterMessage(FromServer.Result)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032edu.cmu.cs.gabriel.networkB\006Protos'))
# @@protoc_insertion_point(module_scope)
