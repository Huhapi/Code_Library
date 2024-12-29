package Final;

public class TicTacView implements View{

	String boardState;
	int[] boards;
	
	public TicTacView() {
		this.boards = new int[9];
		for(int x = 0;x<9;x++)
		{
			this.boards[x] = 0;
		}
		this.boardState = "=========\n"
				+ " "+converter(this.boards[0])+"  "+converter(this.boards[1])+"  "+converter(this.boards[2])+
				"\n "+converter(this.boards[3])+"  "+converter(this.boards[4])+"  "+converter(this.boards[5])+
				"\n "+converter(this.boards[6])+"  "+converter(this.boards[7])+"  "+converter(this.boards[8])+
				"\n=========";
	}
	public void displayBoard()
	{
		System.out.println(this.boardState);
	}
	public void updateBoard(int turn,int spot)
	{
		boards[spot] = turn;
		this.boardState = "=========\n"
				+ " "+converter(this.boards[0])+"  "+converter(this.boards[1])+"  "+converter(this.boards[2])+
				"\n "+converter(this.boards[3])+"  "+converter(this.boards[4])+"  "+converter(this.boards[5])+
				"\n "+converter(this.boards[6])+"  "+converter(this.boards[7])+"  "+converter(this.boards[8])+
				"\n=========";
	}
	
	private String converter(int team)
	{
		if(team == 1)
		{
			return "X";
		}
		if(team == -1)
		{
			return "O";
		}
		if(team == 0)
		{
			return "_";
		}
		return "";
	}
	public void requestMove()
	{
		System.out.println("Select an empty spot on the above board to move:");
	}
	public boolean displayWin(int team) {
		if(team == 1)
		{
			System.out.println("You have Won! This shouldn't be possible...");
			return true;
		}else if(team == -1)
		{
			System.out.println("You have lost.");
			return true;
		}else if(team == 0)
		{
			System.out.println("It was a draw, good job!");
			return true;
		}
		return false;
	}

	
}
