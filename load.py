def load_processed_ids(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        return(lines)

def load_phrases(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    phrases = {}
    for line in lines:
        search, phrase = line.split(';')
        phrases[search] = phrase.strip()

    return(phrases)

def load_subreddits(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        return(lines)

def load_config(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    phrases = {}
    for line in lines:
        search, phrase = line.split(':')
        phrases[search] = phrase.strip()

    return(phrases)

    
