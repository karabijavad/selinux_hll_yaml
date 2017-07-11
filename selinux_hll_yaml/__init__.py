#!/usr/bin/env python
"""Translate YAML to CIL"""

import sys
import yaml

if __name__ == "__main__":
    data = yaml.load(sys.stdin)

    for selinux_user in data.get('users', []):
        print('(user {})'.format(selinux_user))

    for selinux_role in data.get('roles', []):
        print('(role {})'.format(selinux_role))

    for selinux_type in data.get('types', []):
        print('(type {})'.format(selinux_type))
