"""
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.
"""


from numpy import uint16 as uint


class Instruction():
    COMMANDS = 'AND OR NOT LSHIFT RSHIFT ASSIGN'.split()
    def __init__(self, op, receiver, *args):
        if op not in Instruction.COMMANDS:
            raise TypeError('op {} not recognized'.format(op))
        self.op = op
        self.receiver = receiver
        self.args = args
        self.executed = False
        
    def __repr__(self):
        return "<Instruction: {!r}, {!r} -> {!r}>".format(self.op, self.args, self.receiver)
        
    def can_be_run(self, memory):
        return all(isinstance(val, uint) or val in memory for val in self.args)     
        
    def execute(self, memory):
        args = [self.lookup(arg, memory) for arg in self.args]
        if self.receiver in memory:
            self.executed = True
            return memory

        if self.op == 'ASSIGN':
            result = args[0]
        elif self.op == 'OR':
            result = args[0] | args[1]
        elif self.op == 'AND':
            result = args[0] & args[1]
        elif self.op == 'NOT':
            result =  ~args[0]
        elif self.op == 'LSHIFT':
            result = args[0] << args[1]
        elif self.op == 'RSHIFT':
            result = args[0] >> args[1]           

        memory[self.receiver] = result
        self.executed = True
        return memory

    @staticmethod
    def lookup(val, memory):
        return uint(memory.get(val, val))   

def try_int(s):
    return uint(s) if s.isdigit() else s

def input_lines():
    with open('./day_7.input.txt', 'r') as file:
        yield from file.readlines()

# %%
def decompose(line):
    line = line.strip()
    command, receiver = line.split(' -> ')
    command = command.split()

    if len(command) == 1:
        return Instruction('ASSIGN', receiver, try_int(command[0]))
        
    elif len(command) == 2:
        op, arg = command
        arg = try_int(arg)
        return Instruction(op, receiver, arg)

    elif len(command) == 3:
        arg1, op, arg2 = command
        arg1, arg2 = try_int(arg1), try_int(arg2)
        return Instruction(op, receiver, arg1, arg2)

    raise TypeError('could not parse instruction line: {}'.format(line))

def execute_instructions(instructions, memory=None):
    if memory is None:
        memory = {} 
    loop_count = 0

    while not all(i.executed for i in instructions):
        print('loop_count', loop_count)
        
        for instr in instructions:
            if instr.executed:
                continue
            if instr.can_be_run(memory):
                instr.execute(memory)
        loop_count += 1
    return memory             
        
def generate_instructions():
    return [decompose(line) for line in input_lines()]
# %%
#def test():
#    data ='123 -> x\n   456 -> y\n   x AND y -> d\n   x OR y -> e\n   x LSHIFT 2 -> f\n   y RSHIFT 2 -> g\n   NOT x -> h\n   NOT y -> i'
#    data = data.splitlines()
#    deferred = []
#    for line in data:
#        instruction = decompose(line)
#        try:
#            execute(instruction, memory)
#            print('success!')
#        except KeyError:
#            deferred.append(instruction)
#    print('Done reading')
#    temp = []
#    count = 0
#    while len(deferred) != 0:
#        print('loop number:', count, 'deferred:', len(deferred))
#        temp = deferred[:]
#        shuffle(temp)
#        deferred.clear()
#        for instruction in temp:
#            try:
#               # print('trying deferred instruction for {}'.format(instruction.receiver))
#                execute(instruction, memory)
#                print('success!')
#            except KeyError:
#                deferred.append(instruction)
#        count += 1
#        if count > 500:
#            break
    
# %%

if __name__ == '__main__':
    instructions = [decompose(line) for line in input_lines()]
    results = execute_instructions(instructions)
    print(results)