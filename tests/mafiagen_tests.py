from nose.tools import *
from mafiagen import mafiagen

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_template_read():
    result = mafiagen.read_template_file("testfile.txt")
    assert_equal(result, "test file line 1\ntest file line 2\ntest file line 3\n")

def test_setup_read():
    result = mafiagen.read_setup_file("testfile.txt")
    assert_equal(result, ["test file line 1", "test file line 2", "test file line 3"])
    
def test_write_file():
    result = mafiagen.write_file("pudding %s", "is delicious", "testfile.txt")
    assert_equal(result, "pudding is delicious")

def test_setup_to_tuple():
    result = mafiagen.setup_to_tuple(["test game name", "test user name", "test deadline"])
    assert_equal(("test game name", "test user name", "test user name", "test deadline"), result)

def test_setup_complete():
    setuplist = mafiagen.read_setup_file("testfile.txt")
    result = mafiagen.setup_to_tuple(setuplist)
    assert_equal(("test file line 1", "test file line 2", "test file line 2", "test file line 3"), result)
