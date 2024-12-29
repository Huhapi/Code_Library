package Final;

public interface Model {
	// Requires an object implementing this model to call playMove on.
	public int playMove(int spot,int turn); // This takes in the player's int value(1,0 or -1) of the last move, returns the int position of the next move to be played.
	public int[] initBoard(); // Initialize the boardstate
	public void updateBoard(int team,int spot); // Adjust the board state.
	public int getWin(); // Check if win scenario.
	public boolean spotCheck(int spot); // Check if position is empty.
	public boolean endGame(); // End of game check.
}
