# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x63\x61lculator.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\"\x1e\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\"\"\n\x0eSearchResponse\x12\x10\n\x08response\x18\x01 \x01(\t2J\n\nCalculator\x12 \n\nSquareRoot\x12\x07.Number\x1a\x07.Number\"\x00\x12\x1a\n\x04Sine\x12\x07.Number\x1a\x07.Number\"\x00\x32\x44\n\x0cSearchEngine\x12\x34\n\x0fGetSearchAnswer\x12\x0e.SearchRequest\x1a\x0f.SearchResponse\"\x00\x62\x06proto3')
)




_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=20,
  serialized_end=43,
)


_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='SearchRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=45,
  serialized_end=75,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='SearchResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=77,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), dict(
  DESCRIPTOR = _NUMBER,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  ))
_sym_db.RegisterMessage(Number)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRESPONSE,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:SearchResponse)
  ))
_sym_db.RegisterMessage(SearchResponse)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=113,
  serialized_end=187,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='Calculator.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Sine',
    full_name='Calculator.Sine',
    index=1,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR


_SEARCHENGINE = _descriptor.ServiceDescriptor(
  name='SearchEngine',
  full_name='SearchEngine',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=189,
  serialized_end=257,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSearchAnswer',
    full_name='SearchEngine.GetSearchAnswer',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCHENGINE)

DESCRIPTOR.services_by_name['SearchEngine'] = _SEARCHENGINE

# @@protoc_insertion_point(module_scope)
