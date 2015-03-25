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
    result = mafiagen.read_setup_file("testfile.txt")
    assert_equal(result, "test file line 1\ntest file line 2\ntest file line 3\n")
    
def test_write_file():
    result = mafiagen.write_file("pudding %s", "is delicious", "testfile.txt")
    assert_equal(result, "pudding is delicious")
