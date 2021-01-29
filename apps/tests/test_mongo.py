# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from apps.exts.mongodb import db
from apps.exts.schema import ma


class User(db.Document):
    email = db.StringField(required=True)
    username = db.StringField(required=True, max_length=128, unique=True)

    def __repr__(self):
        return 'User(email="{}", username="{}")'.format(self.username, self.password)


class UserSchema(ma.Schema):
    class Meta:
        model = User


def test():
    db.Document()


if __name__ == '__main__':
    test()
