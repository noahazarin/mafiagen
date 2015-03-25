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
    
def test_combine_setup():
    result = mafiagen.combine_setup("pudding %s", "is delicious", "testfile.txt")
    assert_equal(result, "pudding is delicious")

def test_setup_to_tuple():
    result = mafiagen.setup_to_tuple(["test game name", "test user name", "test deadline"])
    assert_equal(("test game name", "test user name", "test user name", "test deadline"), result)

def test_setup_complete():
    setuplist = mafiagen.read_setup_file("testfile.txt")
    result = mafiagen.setup_to_tuple(setuplist)
    assert_equal(("test file line 1", "test file line 2", "test file line 2", "test file line 3"), result)

def test_combined_write():
    setuplist = mafiagen.read_setup_file("testsetup.txt")
    templatestring = mafiagen.read_template_file("testtemplate.txt")
    setuptuple = mafiagen.setup_to_tuple(setuplist)
    result = mafiagen.combine_setup(templatestring, setuptuple, "testtotal.txt")
    resultlist = result.split('\n')
    assert_equal(resultlist[2][11:-13], "test mafia")
    assert_equal(resultlist[4][61:67], "cohost")
    assert_equal(resultlist[4][68:74], "cohost")
    assert_equal(resultlist[101][207:215], "1500 PST")

def test_blank_list():
    result = mafiagen.create_player_list("blanklist.txt")
    resultlist = result.split('\n')
    assert_equal(resultlist[0], "[b]Player List[/b]") 

def test_players_to_tuple():
    result = mafiagen.playerlist_and_url_to_tuple("url", ["player1", "player2"])
    assert_equal(result, ("player1", "url", "player1", "player2", "url", "player2"))

def test_list_population():
    playertuple = mafiagen.playerlist_and_url_to_tuple("url", ["player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8", "player9", "player10", "player11", "player12", "player13"])
    result = mafiagen.populate_player_list("varlist.txt", playertuple, "testpopulatedfile.txt")

def test_newbie_filegen():
    result = mafiagen.generate_initial_newbie_files("testtemplate.txt", "testsetup.txt")
    with open("resources/newbieroles.txt", "r") as f:
        roles = f.read()
    assert_equal(result, roles) 
