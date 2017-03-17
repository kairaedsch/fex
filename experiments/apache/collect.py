#!/usr/bin/env python
from __future__ import absolute_import

from core import collect


def main():
    collect.collect("apache", user_parameters={
        "num_clients": ["Concurrency Level", lambda l: collect.get_int_from_string(l)],
        "tput": ["Requests per second", lambda l: collect.get_float_from_string(l)],
        "lat": ["[ms] (mean)", lambda l: collect.get_float_from_string(l)],
        "complete_requests": ["Complete requests", lambda l: collect.get_int_from_string(l)],
        "failed_requests": ["Failed requests", lambda l: collect.get_int_from_string(l)],
    })
