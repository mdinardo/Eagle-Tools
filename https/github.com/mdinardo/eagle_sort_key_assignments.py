class EagleKeyBinding:
    key = '';
    modifiers = '';
    command = '';

    def __init__(self, inp):
        """
        Init an EagleKeyBinding object.

        Arguments:
            inp:
                A string in the format: Assign <Modifiers>+<Key> <Command>;
        """
        inp = inp.strip('\n').split(' ');
        #filter empty tokens
        inp = [x for x in inp if x is not ''];
        if len(inp) > 2:
            inp[2] = ' '.join(inp[2:]);
            self.command = inp[2];

        key_combo = inp[1].split('+');

        if len(key_combo) > 1:
            #extract modifiers and sort each char to assist with sorting of key bindings
            self.modifiers = ''.join(sorted(key_combo[0]));
        self.key = key_combo[-1];

    def __str__(self):
        return "Assign {0}+{1} {2}".format(self.modifiers, self.key, self.command);

    def __gt__(self, x)
        return ( self.key > x.key or (self.key == x.key && self.modifiers > x.modifiers) );

    def __lt__(self, x)
        return ( self.key < x.key or (self.key == x.key && self.modifiers < x.modifiers) );

    def __eq__(self, x)
        return ( self.key == x.key && self.modifiers == x.modifiers );

def eagle_sort_key_assignments(inp):
    """
    Sorts eagle command assignments.

    Eagle commands are defined like this:
    Assign <Modifiers>+<Key> '<command>';
    Modifiers are a combination of one or more of C (ctrl), A (alt), S (shift)

    Commands are sorted lexicographically first by Key, then by Modifiers

    Arguments:

    inp:
        a multi-line string containing 1 command assignment per line.
        lines must be separated with a newline '\n' character.
    """

    lines = inp.strip('\n').split('\n');
    bindings = [EagleKeyBinding(x) for x in lines];
    bindings.sort()

    for binding in bindings:
        print(binding);
  
