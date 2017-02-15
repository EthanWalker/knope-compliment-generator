import random


# list of adjectives for use in generated quote
adj_list = ['adaptable', 'adorable', 'amazing', 'beautiful', 'brilliant',
            'chestnut-haired', 'compassionate', 'cool under pressure',
            'courageous', 'crazy', 'cunning', 'delicious', 'delightful',
            'devious', 'doe-eyed', 'dynamic', 'elegant', 'exceptional',
            'expensive', 'exuberant', 'generous', 'genius', 'glamorous',
            'glowing', 'good-looking', 'gorgeous', 'graceful', 'handsome',
            'interesting', 'intuitive', 'magical', 'magnificent',
            'misunderstood', 'mysterious', 'naive', 'noble', 'opalescent',
            'organized ', 'passionate', 'perfect', 'persistent', 'pliable',
            'poetic', 'powerful', 'priceless', 'radiant', 'rainbow-infused',
            'rule-breaking', 'sassy', 'scholarly', 'simple', 'smart as a whip',
            'sophisticated', 'stunning', 'stupid hot', 'talented', 'thoughtful',
            'tricky', 'unstoppable', 'whimsical', 'wild', 'wise', 'wondrous',]

# list of nouns for use in generated quote
noun_list = ['baby turtle', 'barrel of monkeys', 'bush baby', 'butterfly',
             'child', 'emperor penguin', 'fluorescent light bulb of truth',
             'house cat', 'human', 'ice sculptor', 'inspiration', 'magician',
             'mannequin come to life', 'mermaid', 'middle school marching band',
             'miniature horse', 'minx', 'monarch butterfly', 'moth', 'musk ox',
             'narwhal', 'newborn baby', 'nymph', 'olympic gymnast', 'penguin',
             'phenomenal well of ideas', 'potted plant', 'rainbow of joy',
             'space unicorn', 'stack of waffles', 'stagecoach driver',
             'stairway to heaven', 'sun goddess', 'sunbonnet', 'sunfish',
             'sunflower', 'swordfish', 'three-toed sloth', 'tiger',
             'trapeze artist', 'treeshark', 'tropical fish', 'unicorn',
             'Victorian mansion', 'Wes Anderson film',]

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
                       "{} you, {}. You're {} and you're {}.".format(name, noun, adj_1, adj_2),
                       "{}, you {}, {} {}.".format(name, adj_1, adj_2, noun),
                       "{} you're {} and I love you!".format(name, adj_1),
                       "Oh {}, you're so {} and {} and {}.".format(name, adj_1, adj_2, adj_3),
                       "{}, you {} {}.".format(name, adj_1, noun),
                       "{}, you {} and {} {}.".format(name, adj_1, adj_2, noun),
                       "{} you are so {}. {} {}.".format(name, adj_1, adj_1, name),
                       "{}, nobody can match your {} energy.".format(name, adj_1),
                       ]
    # create a random quote and return it!
    quote = random.choice(quote_templates)
    return quote
