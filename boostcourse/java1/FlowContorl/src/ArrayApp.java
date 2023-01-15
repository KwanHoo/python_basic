
public class ArrayApp {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//String users = "a,b,c";
		String[] users = new String[3];
		users[0] = "TEST1";
		users[1] = "TEST2";
		users[2] = "TEST3";
		
		int i = 0;
		for(i=0;i<3;i++) {
			System.out.println(users[i]);
		}
		
		System.out.println(users.length);
		
		int[] scores = {10, 100, 200};
		
		System.out.println(scores[1]);
	}

}
