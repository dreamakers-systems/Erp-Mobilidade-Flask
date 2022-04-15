""" Marshmellow schemas to load Json datas """

from marshmallow import Schema


class MotoristJsonSchema(Schema):
    """Marshmellow schema to load motorist datas"""

    class Meta:
        """To serialize Sql Consult"""

        fields = ("id", "name", "data_json")
