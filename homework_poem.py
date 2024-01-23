
import argparse
parser = argparse.ArgumentParser(description='import, change and export of document')
parser.add_argument('-o','--output_file', help='output file', required=True)
parser.add_argument('-i', '--input_file', help='input file', required=True)
parser.add_argument("-u", "--operation_new_word", action="store_true", help=("replace every 4th word in the poem"))

def input_output(input, output,  operation):
    with open('poem1.txt', mode='r', encoding='utf-8') as poem_file:
      #print(poem_file)
      new_list = []
      #temporary_poem= poem_file
      for line in poem_file:
         words = line.split()
         words[3] = "whatever"
         new_line = " ".join(words)
         new_list.append(new_line)
    
    new_poem1 = " ".join(new_list)

    with open(output, mode="w", encoding='utf-8') as new_poem:
       new_poem.write(new_poem1)


args = parser.parse_args()
input_output(args.input_file, args.output_file, args.operation_new_word)