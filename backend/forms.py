from wtforms import StringField, Form


class WriteExcelForm(Form):
    address = StringField('address')


class ReadExcelForm(Form):
    address = StringField('address')


class MergeForm(Form):
    merge_by_column = StringField('merge_by_column')


class ExtractForm(Form):
    extract_column = StringField('extract_column')
