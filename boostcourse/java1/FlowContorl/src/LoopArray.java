
public class LoopArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] users = new String[3];
		users[0] = "TEST1";
		users[1] = "TEST2";
		users[2] = "TEST3";
		
		for(int i=0; i<3; i++) {
			if (i == 2) {
				System.out.println("Finish"+users[i]);
			}else {
			System.out.println("<li>"+users[i]+"</li>");
		}}
	}

}
