#!/usr/bin/env python
"""Translate YAML to CIL"""

import sys
import yaml

if __name__ == "__main__":
    data = yaml.load(sys.stdin)

    print(data)
