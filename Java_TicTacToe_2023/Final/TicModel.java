package Final;

public class TicModel implements Model{
	int[] board;
	TicTacTree cantLose;
	
	public TicModel()
	{
		this.board = initBoard();
	}
	public TicModel(int[] boarder)
	{
		this.board = boarder;
	}
	public int playMove(int spot,int turn)
	{
		this.cantLose = new TicTacTree(this.board,spot,turn);
		return this.cantLose.playMove(board,turn);
		
	}
	public int[] initBoard()
	{
		int[] board = new int[9];
		for(int x = 0;x<9;x++)
		{
			board[x] = 0;
		}
		return board;
	}
	
	public void updateBoard(int team,int spot)
	{
		this.board[spot] = team;
	}
	
	/**
	 * Method getWin
	 * calls the method solved from TicTacTree to determine if a winning scenario has been reached. 
	 */
	public int getWin()
	{
		return cantLose.solved(this.board);
	}
	
	public boolean spotCheck(int spot)
	{
		if(board[spot]!= 0)
		{
			return false;
		}else
		{
			return true;
		}
	}
	public boolean endGame()
	{
		boolean end;
		for(int a: board)
		{
			if(a == 0)
			{
				return false;
			}
		}
		return true;
	}
}
