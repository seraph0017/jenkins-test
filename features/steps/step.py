#!/usr/bin/env python
#encoding:utf-8
from behave import *

@step(u'你是猪')
def step_impl(context):
    assert 1 == 1

@step(u'你是猴')
def step_impl(context):
    assert 2 == 2


@step(u'你肯定认识唐僧')
def step_impl(context):
    assert 3 == 3
