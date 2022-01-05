from field import Field

def main():
    print('rows?')
    user_rows = int(input())
    print('columns?')
    user_columns = int(input())

    game_of_life_board = Field(user_rows,user_columns)

    game_of_life_board.draw_field()
    

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            game_of_life_board.update_field()
            game_of_life_board.draw_field()


main()