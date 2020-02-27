import random
import string
import os

WORD_LEN_RANGE = 1, 15
NUM_WORDS_IN_SENTENCE_RANGE = 3, 10
NUM_SENTENCES_IN_PARA_RANGE = 1, 6

TEXT_WIDTH = 60

class TextGenerator(object):

    @classmethod
    def _generate_word(cls):

        return ''.join(
                [
                    random.choice(string.ascii_lowercase) 
                    for _ in range(random.randint(*WORD_LEN_RANGE))
                ]
            )

    @classmethod
    def _generate_sentence(cls):
        return (' '.join(
            [
                cls._generate_word() 
                for _ in range(random.randint(*NUM_WORDS_IN_SENTENCE_RANGE))
            ]
        ) + '.').capitalize()

    @classmethod
    def _generate_para(cls):
        return " ".join(
            [
                cls._generate_sentence()
                for _ in range(random.randint(*NUM_SENTENCES_IN_PARA_RANGE))
            ]
        )

    @classmethod
    def _format_para(cls, para, max_width):
        result = []
        
        word_gen = (word for word in para.split())
        line = ''
        while True:
            try:
                word = next(word_gen)
                if len(line) + len(word) + 1 > max_width:
                    result.append(line)
                    line = word + ' '
                else:
                    line = line + word + ' '

            except StopIteration:
                result.append(line)
                return result

    @classmethod
    def get_formatted_para_as_list(cls, width=TEXT_WIDTH):
        para = cls._generate_para()
        return cls._format_para(para, width)

    @classmethod
    def get_formatted_para_as_str(cls, width=TEXT_WIDTH):
        return os.linesep.join(cls.get_formatted_para_as_list(width))


if __name__ == '__main__':

    result = TextGenerator.get_formatted_para_as_list()

    print("Print random text from list of lines.")
    for line in result:
        print(line)

    print()
    print("Print the same text as one line.")
    print(os.linesep.join(result))
    

