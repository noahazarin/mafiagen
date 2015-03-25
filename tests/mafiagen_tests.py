from nose.tools import *
from mafiagen import mafiagen

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_template_read():
    mafiagen.read_template_file()

def test_setup_read():
    mafiagen.read_setup_file()

def test_write_file():
    result = mafiagen.write_file("pudding %s", "is delicious", "testfile.txt")
    assert_equal(result, "pudding is delicious")
