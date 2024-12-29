package Final;

public class Main {

	public static void main(String[] args) {
		
		GameController game = new TicTacControl();
		game.go();
		
		//int[] newboard = {1,-1,1,1,-1,-1,0,1,0};
		//TicTacTree node1 = new TicTacTree(newboard, 8,1);
		//Model runitt = new TicModel(newboard);
		//System.out.println("Next move is: "+Integer.toString(runitt.playMove(3,1)));
		//System.out.println(node1.getString());

	}

}