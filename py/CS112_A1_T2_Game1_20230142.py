
#Purpose:A 100 game in python.Two players take turns adding numbers from 1 to 10 to a running sum. The first player to reach 100 wins.
#Author : Roaa Mohammed Sayed


# welcome message
print("**** welcome to 100 game**** ")
print("In this game, two players will take turns adding numbers between 1 and 10 to a running total.")
print("The first player to reach a total sum of 100 wins the game.")
print("Let's get started!")
# Initialize the total sum of moves
total_sum = 0

# Main game loop
while total_sum < 100:
    while True: # Start a loop to handle Player 1's move input
        move = input("Player 1: Please enter a number between 1-10: ")
        if move.isdigit():
            move = int(move)
            if move > 0 and move <= 10:  # Check if the move is within the valid range
                if total_sum + move > 100: # Ensure the total sum does not exceed 100
                    print("Player 1, you cannot exceed 100. Try again.")
                    continue
                total_sum += move
                print("The sum is now", total_sum)  # Update and Display the current total sum
                break  # Exit the loop for Player 1's move input
            else:
                print("Invalid number")
        else:
            print("Invalid input. Please enter a valid number.")

    # Check if Player 1 won after making a move
    if total_sum == 100:
        print("Player 1 wins!")
        break # Exit the main loop if player 1 won

    while True: # Start a loop to handle Player 2's move input
        move = input("Player 2: Please enter a number between 1-10: ")
        if move.isdigit():
            move = int(move)
            if move > 0 and move <= 10:  # Check if the move is within the valid range
                if total_sum + move > 100:  # Ensure the total sum does not exceed 100
                    print("Player 2, you cannot exceed 100. Try again.")
                    continue
                total_sum += move
                print("The sum is now", total_sum)  # Display the current total sum
                break  # Exit the loop for Player 2's move input
            else:
                print("Invalid number")
        else:
            print("Invalid input. Please enter a valid number.")

    # Check if Player 2 won after making a move
    if total_sum == 100:
        print("Player 2 wins!")
        break # Exit the main loop if player 2 won


