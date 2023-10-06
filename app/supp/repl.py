
import traceback
from supp.config import todo

try:
    import readline
except:
    pass 

def repl(prompt):

    while True:

        try:
            user_input = input(prompt)

        except EOFError:
            print('')
            break        

        if not user_input.strip():
            continue

        input_strings = user_input.split(maxsplit=1)

        command = input_strings[0].lower()

        try:

            if len(input_strings) == 1:

                if command in ('exit', 'quit'):
                    break

            if len(input_strings) == 2:

                param = input_strings[1]

                if command == 'genre':

                    count, films = todo['films'].get_by_genre(param)
                    print(films)
                    print(f'{count} film(s) retrieved.')

                    continue

                if command == 'director':

                    count, films = todo['films'].get_by_director(param)
                    print(films)
                    print(f'{count} film(s) retrieved.')

                    continue
                
            raise AssertionError

        except AssertionError:
            print('Usage: { genre <genre> | director <director> | exit|quit }')

        except Exception as err:
            print(err)
            traceback.print_exc()
