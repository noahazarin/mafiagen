def read_template_file():
    '''
    read file containing information about default rules that don't change 
    '''
    pass

def read_setup_file(filename):
    '''
    read file containing setup specific, like number of mafia, number of town, and so on.
    '''
    result = []
    with open("ini/%s" % filename, "r") as f:
        for line in f:
            result.append(line)
    return ''.join(result)

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


