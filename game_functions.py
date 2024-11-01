import game_functions as gf

def main():
    grid = gf.initialize_grid()
    gf.display_grid(grid)

    while True:
        try:
            # Capture user input
            move = input("Enter move (w/a/s/d to move, q to quit): ").strip().lower()

            # Validate input
            if move not in ['w', 'a', 's', 'd', 'q']:
                raise ValueError("Invalid input! Please enter 'w', 'a', 's', 'd' to move, or 'q' to quit.")

            # Handle quit option
            if move == 'q':
                print("Game over!")
                break

            # Execute the move based on user input
            if move == 'w':
                gf.move_up(grid)
            elif move == 's':
                gf.move_down(grid)
            elif move == 'a':
                gf.move_left(grid)
            elif move == 'd':
                gf.move_right(grid)

            # Add a new number after each valid move
            gf.add_new_number(grid)
            gf.display_grid(grid)

            # Check for win or game over conditions
            if gf.check_win(grid):
                print("Congratulations! You've reached 2048! You win!")
                break
            elif gf.check_game_over(grid):
                print("No more moves available! Game over.")
                break

        except ValueError as ve:
            # Handle invalid input error
            print(ve)

if __name__ == "__main__":
    main()
