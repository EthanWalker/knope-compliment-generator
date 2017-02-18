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
    # set 3 adj from a random sample
    adj_1, adj_2, adj_3 = random.sample(adj_list, 3)
    # create a capitalized version of adj_1 for our special case
    adj_1_cap = adj_1.capitalize()
    # set a noun
    noun = random.choice(noun_list)
    # set of quote templates for variety
    quote_templates = ["Oh {name}, you {adj_1}, {adj_2}, {adj_3} {noun}.",
                       "{name}, you {noun}. You're {adj_1} and you're {adj_2}.",
                       "{name}, you {adj_1}, {adj_2} {noun}.",
                       "{name} you're {adj_1} and I love you!",
                       "Oh {name}, you're so {adj_1} and {adj_2} and {adj_3}.",
                       "{name}, you {adj_1} {noun}.",
                       "{name}, you {adj_1} and {adj_2} {noun}.",
                       "{name} you are so {adj_1}. {adj_1_cap} {name}.",
                       "{name}, nobody can match your {adj_1} energy.",]
    # create a random quote and return it!
    return random.choice(quote_templates).format(**vars())