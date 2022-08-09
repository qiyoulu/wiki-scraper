import glob
import pynlpir
import matplotlib.pyplot as pyplot
import pandas

def parse():
    pynlpir.open()
    pyplot.rcParams.update({'font.size': 8})
    for filename in glob.glob('*.txt'):
        f = open((filename), 'r', encoding='utf-8')
        print(filename)
        text = f.read()
        keywords = pynlpir.get_key_words(text, weighted=True)
        data = pandas.DataFrame(keywords, columns=['word', 'frequency'])
        data.plot(kind='bar', x='word')
        pyplot.subplots_adjust(bottom=0.25)
        pyplot.savefig(filename.split('.')[0] + '.jpg')
    pynlpir.close()

if __name__ == '__main__':
    parse()