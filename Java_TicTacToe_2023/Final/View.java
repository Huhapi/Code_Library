package Final;

public interface View {
	public void displayBoard();
	public void updateBoard(int turn, int spot); // The player's turn and spot they played.
	public void requestMove();
	public boolean displayWin(int team);
	
}
