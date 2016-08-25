import webbrowser
from easy_class import CLASSIFICATION


# --- DEFAULT --- #
DEF_FILE_NAME = 'segment-ac.txt'
DEF_OUTPUT_NAME = 'segment-ac-output.txt'
DEF_START = 0

file_name = input('Please type filename: ')
if len(file_name) == 0:
    file_name = DEF_FILE_NAME

start = input('Start from? ')
if len(start) == 0:
    start = DEF_START   

def classification(file_name, counter):
    ''' Func for classification non-profit sites based on <...> '''
    try:
        with open(file_name) as f:
            site_list = f.read().splitlines()

            for x in range(counter, len(site_list), +1):
                url = site_list[counter]
                webbrowser.open_new_tab('http://' + url + '/')

                print('# --- CURRENT SITE --- #')
                print('http://' + url)

                category1 = input('Please type category and press ENTER: ')
                category2 = ''

                if category1 == '2':
                    category1 = input('Please type category 1 and press ENTER: ')
                    category2 = input('Please type category 2 and press ENTER: ')

                if category1 == 'S':
                    print('Save file and close program. Buy!')
                    break

                while category1 not in CLASSIFICATION.keys():
                    category1 = input('Please type CORRECT category and press ENTER: ')

                if category2 == '':
                    site_list[counter] = str(counter) + '\t' + url + '\t' + category1
                else:
                    site_list[counter] = str(counter) + '\t' + url + '\t' + category1 + '\t' + category2


                print(site_list[counter], '-->', CLASSIFICATION[category1])
                print('')

                counter += 1

            with open(DEF_OUTPUT_NAME, 'w') as output_file:
                for line in site_list:
                    output_file.write(line + '\n')

    except Exception as e:
        print(e)


# --- TEST --- #
classification(file_name, int(start))