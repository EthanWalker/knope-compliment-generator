import random


# list of adjectives for use in generated quote
adj_list = ['adaptable', 'amazing', 'crazy', 'beautiful', 'compassionate',
            'courageous', 'cunning', 'exceptional', 'exuberant', 'graceful',
            'generous', 'gorgeous','intuitive', 'magnificent', 'naive',
            'passionate', 'persistent', 'pliable', 'radiant', 'rule-breaking',
            'sophisticated', 'stunning', 'talented', 'whimsical', 'wild',
            'elegant', 'good-looking', 'dynamic', 'mysterious', 'delicious',
            'glowing', 'chestnut-haired', 'scholarly', 'wise', 'poetic',
            'noble', 'powerful', 'brilliant', 'thoughtful', 'stupid hot',
            'doe-eyed', 'magical']

# list of nouns for use in generated quote
noun_list = ['unicorn', 'mermaid', 'narwhal', 'tiger', 'sunfish', 'swordfish',
             'nymph', 'middle school marching band', 'ice sculptor', 'human',
             'potted plant', 'newborn baby', 'moth', 'minx', 'musk ox',
             'trapeze artist', 'butterfly', 'monarch butterfly', 'penguin',
             'emperor penguin', 'three-toed sloth', 'bush baby',
             'olympic gymnast', 'baby turtle', 'stagecoach driver',
             'Wes Anderson film', 'stack of waffles', 'sunflower',
             'Victorian mansion', 'sun goddess']

def generate_quote(name):
    '''
    Generate custom quote in the style of Leslie Knope using user name

    :param name: string name
    :return: string quote
    '''
    adj_1 = random.choice(adj_list)
    # set a 2d adjective and make sure it isn't the same as the first
    adj_2 = random.choice(adj_list)
    while adj_1 == adj_2:
        adj_2 = random.choice(adj_list)
    # set a 3rd adjective and make sure it  isn't the same as the first 2
    adj_3 = random.choice(adj_list)
    while adj_1 == adj_3 or adj_2 == adj_3:
        adj_3 = random.choice(adj_list)
    # set a noun
    noun = random.choice(noun_list)
    # set of quote templates for variety
    quote_templates = ["Oh {}, you {}, {}, {} {}.".format(name, adj_1, adj_2, adj_3, noun),
                       "{} you, {}. You’re {} and you’re {}.".format(name, noun, adj_1, adj_2)]
    # create a random quote and return it!
    quote = random.choice(quote_templates)
    return quote