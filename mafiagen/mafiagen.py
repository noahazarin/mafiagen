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
    read file containing setup specifics, like number of mafia, number of town, and so on.
    '''
    result = []
    with open("resources/%s" % filename, "r") as f:
        for line in f:
            result.append(line[:-1])
    return result

def write_file(poststring, params, filename):
    '''
    write files with final mafia setup posts to /tmp
    uses poststring % params, so pass params as a tuple if sending more than one variable (which is pretty much always) 
    '''
    with open("tmp/%s" % filename, "w+") as f:
        outlines = poststring % params
        f.write(poststring % params)
        f.seek(0)
        result = f.read()
        f.close()
    return result 

def setup_to_tuple(setupstr):
    '''
    convert setup information to tuple

    setup format:
    game name
    cohost name
    deadline (format: 1600 PST)

    cohost name is used twice
    '''
    setuplist = setupstr
    resulttuple = (setuplist[0], setuplist[1], setuplist[1], setuplist[2])
    return resulttuple
