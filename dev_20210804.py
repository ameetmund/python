# File

from translate import Translator

def lang_trans(in_file, out_file):
    input_file = in_file
    output_file = out_file
    translator = Translator(to_lang='hi')
    try:
        with open(input_file, mode='r') as my_file:
            line = my_file.read()
            translation = translator.translate(line)
            with open(output_file, mode='w') as my_out_file:
                my_out_file.write(translation)
    except FileNotFoundError:
        print("File does not exist")


lang_trans('F:\\Python\\PythonProject\\Github\\python\\data\\language.txt',
           'F:\\Python\\PythonProject\\Github\\python\\data\\output.txt')


