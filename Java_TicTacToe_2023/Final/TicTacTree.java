/*
 * Daniel Hayes
 * 11/19/23
 */
package Final;

import java.util.ArrayList;


public class TicTacTree {
	
	private ArrayList<TicTacTree> treeList;
	private int turn;
	private static int count;
	private int numb;
	private int win;
	private int move;
	private int prevMove;
	private int team;
	
	public TicTacTree(int[] board, int thismove, int turn1)
	{
		this.prevMove = thismove;
		count ++;
		this.numb = count;
		this.turn = turn1;
		this.win = 0;
		this.team = turn1*-1;
		extendTree(board,turn1);
		
	}
	public TicTacTree(int[] board, int thismove, int turn1, int wincon)
	{
		this.prevMove = thismove;
		count ++;
		this.numb = count;
		this.turn = turn1;
		this.win = wincon;
		this.team = turn1*-1;
	}
	public TicTacTree(int[] board, int thismove, int turn1, boolean firstturn)
	{
		this.prevMove = thismove;
		count ++;
		this.numb = count;
		this.turn = turn1;
		this.win = 0;
		this.team = turn1*-1;
		if(board[4] == 0)
		{
			this.move = 4;
		}else
		{
			this.move = 0;
		}
		
	}
	public int branchCount()
	{
		return 1+treeList.size();
	}
	/**
	 * extendTree is used recursively with one of the TicTacTree constructors
	 * to create the tree of possible moves for a tic tac toe game.
	 * @param int[] state is the current board state.
	 * @param turn determine's who's turn it is -1 or 1.
	 */
	public void extendTree(int[] state,int turn)
	{
		
		boolean firstnode = false;
		int x;
		for(x = 0; x<9; x++)
		{
			if(state[x]==0) // For every spot on the board, for each empty spot, do this:
			{
				int[] newstate = state.clone();
				newstate[x] = turn*-1; // The turn value stores the value used in the array for that player capturing a square.
				if(solved(newstate)== 0) // If this new board state doesn't create a 3 in a row:
				{
					if(!firstnode)
					{
						TicTacTree node = new TicTacTree(newstate, x,-1*turn);
						this.treeList = new ArrayList<TicTacTree>();
						this.treeList.add(node);
						firstnode = true;
					}else
					{
						TicTacTree newNode = new TicTacTree(newstate, x,-1*turn);
						
						this.treeList.add(newNode);
					}
				}else if(solved(newstate)== 1)
				{
					if(!firstnode)
					{
						this.treeList = new ArrayList<TicTacTree>();
						this.treeList.add(new TicTacTree(newstate, x,-1*turn, 1));
						firstnode = true;
					}else
					{
						TicTacTree newerNode = new TicTacTree(newstate, x,-1*turn, 1);
						treeList.add(newerNode);
					}
				}else if(solved(newstate)== -1)
				{
					if(!firstnode)
					{
						this.treeList = new ArrayList<TicTacTree>();
						treeList.add(new TicTacTree(newstate, x,-1*turn, -1));
						firstnode = true;
					}else
					{
						TicTacTree newerNode = new TicTacTree(newstate, x,-1*turn, -1);
						treeList.add(newerNode);
					}
				}
				
			}
		}
	}
	public int getPrevMove()
	{
		return this.prevMove;
	}
	/**
	 * solved takes in the board state and returns whether or not there is a three in a row.
	 * @param boardstate is the current board state.
	 * @return returns -1 if the -1 player has a 3 in a row, 1 if the 1 player has 3 in a row, or 0
	 * if neither have a win.
	 */
	public static int solved(int[] boardstate)
	{
		if(boardstate[0]+boardstate[1]+boardstate[2] == 3 || boardstate[3]+boardstate[4]+boardstate[5] == 3 ||
				boardstate[6]+boardstate[7]+boardstate[8] == 3 || boardstate[0]+boardstate[3]+boardstate[6] == 3 ||
						boardstate[1]+boardstate[4]+boardstate[7] == 3 || boardstate[2]+boardstate[5]+boardstate[8] == 3 ||
								boardstate[0]+boardstate[4]+boardstate[8] == 3 || boardstate[2]+boardstate[4]+boardstate[6] == 3)
		{
			return 1;
		}else if(boardstate[0]+boardstate[1]+boardstate[2] == -3 || boardstate[3]+boardstate[4]+boardstate[5] == -3 ||
				boardstate[6]+boardstate[7]+boardstate[8] == -3 || boardstate[0]+boardstate[3]+boardstate[6] == -3 ||
						boardstate[1]+boardstate[4]+boardstate[7] == -3 || boardstate[2]+boardstate[5]+boardstate[8] == -3 ||
								boardstate[0]+boardstate[4]+boardstate[8] == -3 || boardstate[2]+boardstate[4]+boardstate[6] == -3)
		{
			return -1;
		}else
		{
			return 0;
		}
	}
	
	/**
	 * Method playMove, to get the next move in position (int) form.
	 * @return the integer placement of the next move.
	 */
	public int playMove(int[] board,int turn)
	{
		int counter = 0;
		for(int a: board)
		{
			if(a==0)
			{
				counter++;
			}
		}
		if(counter == 8)
		{

			if(board[4]!= 1)
			{
				return 4;
			}else
			{
				return 0;
			}
		}
		Wincon getspot = nextMove(turn);
		
		return(getspot.getSpot());
	}
	/**
	 * nextMove method traverses the tree to determine the next move.
	 * @return int, the position of the next move to make.
	 */
	public Wincon nextMove(int turn)
	{
		
		if(treeList != null)
		{
			int length = treeList.size();
			
			Wincon[] scores = new Wincon[length];
			// Iterating through the list of nodes and recursively calling this function on the empty spaces.
		  	for(int x = 0; x<length;x++) 
		  	{
		  		TicTacTree treenode = this.treeList.get(x);
		  		scores[x] = treenode.nextMove(turn*-1);
		  	}
		  	Wincon tracker = scores[0];
		  	//Selecting the best Wincon out of the returned Wincons to return.
		  	for(int y = 1;y<length;y++)
		  	{
			  	if(scores[y].getWin() > tracker.getWin() && scores[y].getDepth() <= tracker.getDepth())
			  	{
			  		tracker = scores[y];
			  	//}else if (scores[y].getWin() == tracker.getWin() && scores[y].getDepth() <= tracker.getDepth())
			  	//{
			  		//tracker = scores[y];
			  	}else 
			  	if(scores[y].getWin()>0 && scores[y].getDepth() < tracker.getDepth())
			  	{
			  		tracker = scores[y];
			  	}
		  	}

		  	tracker.addDepth(); // Tracking the turn at which the win or loss scenario happened. The smaller the depth, the more important.
		  	return tracker;
		}else // This is the base case, leaves on the tree, which are either 3 in a rows, or draws.
		{
			// Return a 99 value if it is a win for computer's team.
			if(this.win == this.team)
			{
				return (new Wincon(this.prevMove,99));
			}else if(this.win == this.team*-1) //Return a 98 value if win for opponent.
			{
				return(new Wincon(this.prevMove,98));
			}else if(this.win == 0)// return 0 for drawn outcome.
			{
				return(new Wincon(this.prevMove,0));
			}
		}
		System.out.println("If this prints, this.win is != to 1,0 or -1.");
		return(new Wincon(this.prevMove,0));

	}
	
	/**
	 * Determins what information is shown on the toString.
	 * @return A String representation of this possible move.
	 */
	public String getString()
	{
		String adder = "";
		for(TicTacTree a: this.treeList)
		{
			adder += a.toString();
		}
		return("["+Integer.toString(this.win)+Integer.toString(this.prevMove)+"] \n"+adder);
	}
	
	/**
	 * Traverses the tree to combine each node's getString.
	 */
	public String toString()
	{
		if(this.treeList != null) {
			
			return(getString());
			
		}else
		{
			if(this.win == -1)
			{
				return("{"+Integer.toString(this.turn)+" "+Integer.toString(this.prevMove)+"} "+"[-1]");
			}else if(this.win == 1)
			{
				return("{"+Integer.toString(this.turn)+" "+Integer.toString(this.prevMove)+"} "+"[1]");
			}else
			{
				return("{"+Integer.toString(this.turn)+" "+Integer.toString(this.prevMove)+"} "+"Draw");
			}
		}
	}
	
}
