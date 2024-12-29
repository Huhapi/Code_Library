package Final;

public class Wincon {
	private int spot;
	private int depth;
	private int win;
	/**
	 * Wincon initiator
	 * @param spotter - the move position - needed to know where to move.
	 * @param thedepth - how many moves back - needed to know which Wincon is sooner.
	 * @param winvalue - -1, 0 or 1 depending on who's winning - needed to know
	 * which position to pick if thedepth is equal, if it has the choice to block
	 * or create a 3 in a row, to know to pick the 3 in a row.
	 */
	public Wincon(int spotter, int winvalue)
	{
		this.spot = spotter;
		this.depth = 0;
		this.win = winvalue;
	}
	/**
	 * Get methods for the three stored values.
	 * @return the move spot.
	 */
	public int getSpot()
	{
		return this.spot;
	}
	/**
	 * Get methods for the three stored values.
	 * @return the depth tracker.
	 */
	public int getDepth()
	{
		return this.depth;
	}
	/**
	 * Get methods for the three stored values.
	 * @return the win value.
	 */
	public int getWin()
	{
		return this.win;
	}
	/**
	 * add Depth method for this win condition.
	 * 
	 */
	public void addDepth()
	{
		this.depth++;
	}
	
}
