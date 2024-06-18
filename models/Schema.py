from marshmallow import fields, Schema

class MovieSchema(Schema):
	id = fields.Int(dump_only=True)
	title = fields.Str(required=True)
	genre = fields.Str(required=True)
	cast = fields.Str(required=True)
	img = fields.Str(required=True)
	amount = fields.Str(required=True)
	available = fields.Str(required=True)
	qty = fields.Str(required=True)



class ContentSchema(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str(required=True)
	types = fields.Str(required=True)
	content = fields.Str(required=True)


class ServiceSchema(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str(required=True)
	desc = fields.Str(required=True)
	image_p = fields.Str(required=True)


class BookedSchema(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str(required=True)
	service = fields.Str(required=True)
	contact_no = fields.Str(required=True)
	booked_date = fields.Str(required=True)
	is_confirm = fields.Str(required=True)
