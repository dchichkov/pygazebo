# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import header_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='vector3d.proto',
  package='gazebo.msgs',
  serialized_pb='\n\x0evector3d.proto\x12\x0bgazebo.msgs\x1a\x0cheader.proto\"+\n\x08Vector3d\x12\t\n\x01x\x18\x02 \x02(\x01\x12\t\n\x01y\x18\x03 \x02(\x01\x12\t\n\x01z\x18\x04 \x02(\x01')




_VECTOR3D = descriptor.Descriptor(
  name='Vector3d',
  full_name='gazebo.msgs.Vector3d',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='gazebo.msgs.Vector3d.x', index=0,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='gazebo.msgs.Vector3d.y', index=1,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='z', full_name='gazebo.msgs.Vector3d.z', index=2,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=45,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['Vector3d'] = _VECTOR3D

class Vector3d(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VECTOR3D
  
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Vector3d)

# @@protoc_insertion_point(module_scope)