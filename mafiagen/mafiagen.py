def read_template_file(filename):
    '''
    read file containing information about default rules that don't change 
    '''
    result = []
    with open("resources/%s" % filename, "r") as f:
        result = f.read()
    return result

def read_setup_file(filename):
    '''
    read file containing setup specifics, like number of mafia, 
    number of town, and so on.
    '''
    result = []
    with open("resources/%s" % filename, "r") as f:
        for line in f:
            result.append(line[:-1])
    return result

def combine_setup(poststring, params, filename):
    '''
    write files with final mafia setup posts to /tmp
    uses poststring % params, so pass params as a tuple if 
    sending more than one variable (which is pretty much always) 
    '''
    with open("tmp/%s" % filename, "w+") as f:
        outlines = poststring % params
        f.write(poststring % params)
        f.seek(0)
        result = f.read()
        f.close()
    return result 

def setup_to_tuple(setuplist):
    '''
    convert setup information to tuple

    setup format:
    game name
    cohost name
    deadline (format: 1600 PST)

    cohost name is used twice
    '''
    resulttuple = (setuplist[0], setuplist[1], setuplist[1], setuplist[2])
    return resulttuple

def create_player_list(filename):
    '''
    generate blank player list file
    '''
    blanklist = read_template_file("blanklist.txt")
    with open("tmp/%s" % filename, "w+") as f:
        f.write(blanklist)
        f.seek(0)
        result = f.read()
        f.close()
    return result

def playerlist_and_url_to_tuple(gameurl, playerlist):
    '''
    13 player setup requires player name, thread url, 
    then player name again for each player.
    '''
    result = []
    for player in playerlist:
        result.append(player)
        result.append(gameurl)
        result.append(player)
    tupleresult = tuple(result)
    return tupleresult

def populate_player_list(template, signuptuple, filename):
    '''
    13-player list with filters
    varlist formatting needs player name, thread url, 
    then player name again    for each player
    '''
    varlist = read_template_file(template)
    with open("tmp/%s" % filename, "w+") as f:
        f.write(varlist % signuptuple)
        f.seek(0)
        result = f.read()
        f.close()
    return result
    
def generate_initial_newbie_files(templatename, setupinfo, signupoutfilename=None, rolesoutfilename=None, setupoutfilename=None):
    '''
    with a template name and the setup info name, generate all the files 
    needed for a game of mafia, including blank signup list.
    for use with newbie games. write these files to tmp
    '''
    if not signupoutfilename:
        signupoutfilename = "newbiesignups.txt"
    if not rolesoutfilename:
        rolesoutfilename = "newbieroles.txt"
    if not setupoutfilename:
        setupoutfilename = "newbiesetup.txt"
    create_player_list(signupoutfilename)
    combine_setup(read_template_file(templatename), setup_to_tuple(read_setup_file(setupinfo)), setupoutfilename)
    with open("resources/newbieroles.txt", "r") as f:
        roles = f.read()
    with open("tmp/%s" % rolesoutfilename, "w+") as f:
        f.write(roles)
    return roles
