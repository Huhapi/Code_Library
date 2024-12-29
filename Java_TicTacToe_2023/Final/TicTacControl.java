/*
 * Daniel Hayes
 * 12/4/23
 * Final Project, Controller for Tic Tac Toe.
 */
package Final;

import java.util.Scanner; 

public class TicTacControl implements GameController{

	private View showTime;
	private Model ticModel;
	
	public TicTacControl()
	{
		this.showTime = new TicTacView(); 
		this.ticModel = new TicModel();
	}
	
	public void go()
	{
		Scanner move = new Scanner(System.in);
		boolean run = true;
		while(run)
		{
			this.showTime.displayBoard();
			

			int spot = 10;
			while(spot == 10) // Assumes numeric input.
			{
				this.showTime.requestMove();
				String thismove = move.nextLine();
				spot = correct(toNumeric(thismove));
				if(spot!=10)
				{
					if(!ticModel.spotCheck(spot))
					{
						spot = 10;
					}
				}
			}
			this.showTime.updateBoard(1, spot);
			this.ticModel.updateBoard(1, spot);
			if(ticModel.getWin()!=0)
			{
				this.showTime.displayBoard();
				this.showTime.displayWin(1);
				run = false;
			}
			if(ticModel.endGame() && ticModel.getWin()==0)
			{
				this.showTime.displayBoard();
				this.showTime.displayWin(0);
				run = false;
			}else
			{
				int mover = this.ticModel.playMove(spot,1);
				this.showTime.updateBoard(-1, mover);
				this.ticModel.updateBoard(-1, mover);
				if(ticModel.getWin()!=0)
				{
					this.showTime.displayBoard();
					this.showTime.displayWin(-1);
					run = false;
				}
			}
		}
		move.close();
	}
	
	/**
	 * Checks an integer value and returns 10 if it is below 0 or above 8.
	 * Otherwise returns the value.
	 * 
	 * @param int color value
	 * @return int value in between parameters.
	 */
	public static int correct(int number) {
		if(number >= 0 && number <= 8) {
			return number;
		}else {
			return 10;
		}
	}
	
	/**
	 * Method to take a String value and return numeric.
	 * 
	 * @param String value
	 * 
	 * @return intValue - the numeric value stored in the String.
	 */
	public static int toNumeric(String value) {
		int intValue;
		try {
			intValue = Integer.parseInt(value);
		}catch(Exception e)
		{
			intValue = 10;
		}
		
		return intValue;
	}
}
