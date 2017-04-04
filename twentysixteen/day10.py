from common import load_data

output = {}

def extract(data, sentinel):
    for idx, item in enumerate(data):
        if item.startswith(sentinel):
            target = idx
            break
    return data.pop(target)

class Bot:
    all_bots = {}

    def __init__(self, num):
        self.id = int(num)
        self.chips = []
        Bot.all_bots[self.id] = self

    def __repr__(self):
        return '<Bot id:{}>'.format(self.id)

    @classmethod
    def find(cls, id):
        return cls.all_bots[int(id)]

    @classmethod
    def get_or_create(cls, id):
        id = int(id)
        try:
            return cls.all_bots[id]
        except KeyError:
            return cls(id)

    def receives(self, chip):
        self.chips.append(chip)
        assert len(self.chips) < 3

        # win condition
        if 61 in self.chips and 17 in self.chips:
            print("WINNER WINNER")
            print("BOT #", self.id)

    @property
    def ready(self):
        return len(self.chips) == 2

    def extract_lowest(self):
        low = min(self.chips)
        self.chips.remove(low)
        return low

    def extract_high(self):
        high = max(self.chips)
        self.chips.remove(high)
        return high

    def gives_low_to(self, bot):
        if not isinstance(bot, self.__class__):
            bot = Bot.get_or_create(bot)

        lowest = self.extract_lowest()
        bot.receives(lowest)

    def gives_high_to(self, bot):
        if not isinstance(bot, self.__class__):
            bot = Bot.get_or_create(bot)
        highest = self.extract_high()
        bot.receives(highest)


def main1():
    setup, instructions = [], []
    for line in load_data():
        if line.startswith('value'):
            setup.append(line)
        else:
            instructions.append(line)

    for line in setup:
        words = line.split()
        val = int(words[1])
        bot = words[-1]
        Bot.get_or_create(bot).receives(val)

    while instructions:
        for bot in list(Bot.all_bots.values()):
            if bot.ready:
                sentinel = 'bot {} gives low'.format(bot.id)
                instruction = extract(instructions, sentinel)
                text = instruction.split()
                if text[5] == 'bot':
                    low_recv = Bot.get_or_create(text[6])
                    bot.gives_low_to(low_recv)
                else:
                    # reciever is output
                    position = int(text[6])
                    output[position] = bot.extract_lowest()

                if text[10] == 'bot':
                    high_recv = Bot.get_or_create(text[11])
                    bot.gives_high_to(high_recv)
                else:
                    position = int(text[11])
                    output[position] = bot.extract_high()





if __name__ == '__main__':
    main1()
    # Part 2:
    # What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?
    total = output[0] * output[1] * output[2]
    print(total)