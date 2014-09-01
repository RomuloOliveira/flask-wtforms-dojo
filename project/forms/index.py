#!/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import *

class IndexForm(Form):
    username = StringField(
        'Username',
        [
            validators.Required(message="Campo obrigatorio"),
            validators.Length(min=4, max=32, message="Username invalido")
        ]
    )

    password = PasswordField(
        'Senha',
        [
            validators.Required(message="Campo obrigatorio"),
            validators.Length(min=4, max=32, message="Senha invalida")
        ]
    )

    submit = SubmitField('>')
