
'''
EDIS / Assignment 6
'''


if __name__ == '__main__':


    '''
    Parse arguments
    '''

    from  argparse import ArgumentParser

    parser = ArgumentParser(
        description='Assignment 6'
    )

    parser.add_argument(
        '-r', '--review', choices=['0', '1', '2'], default='0',
        help='whose code is being run, default: 0 (your code)'
    ) 
    args = vars(parser.parse_args())


    '''
    Import modules and update config
    '''

    from supp.repl import repl

    if args['review'] == '1':
         from todos.review_1 import films 
    elif args['review'] == '2':
         from todos.review_2 import films
    else:
         from todos.your_code import films 

    import supp.config
    supp.config.todo['films'] = films     


    '''
    Run REPL
    '''

    todo_folder = 'your_code' if not int(args.get('review')) else f'review_{args["review"]}'
    repl(prompt = f'[{todo_folder} / films] > ')
