#!/usr/bin/env python

import os
import sys

count = int(sys.argv[1])

test_output_template = '''<?xml version="1.0" encoding="utf-8"?>
<testsuites>
    <testsuite errors="0" failures="0" hostname="c33539e58e16" name="pytest-{0}" skipped="0" tests="1" time="{0}" timestamp="2020-09-14T21:06:17.179664">
        <testcase classname="test_case" name="test_function_{0}" time="{0}"></testcase>
    </testsuite>
</testsuites>
'''

d = os.environ.get('SYSTEM_DEFAULTWORKINGDIRECTORY', '')
for i in range(count):
    filename = os.path.join(d, 'test-{}.xml'.format(i))
    open(filename, 'w').write(test_output_template.format(i))
    print(
        "##vso[results.publish type=JUnit;runTitle='Some Test {}';]{}".format(
            i, filename,
        )
    )

