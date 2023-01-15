
public class AuthApp3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// String[] users = {"Ralo", "Paka", "Dopa"};
		String[][] users = {
				{"Ralo", "1111"},
				{"Paka", "2222"},
				{"Dopa", "3333"},
		};
		String inputId = args[0];
		String inputPass = args[1];
		//testing
		
		// flag
		boolean isLogined = false;
		for(int i=0; i<users.length; i++){
			String[] current = users[i];
			
			// System.out.println(users[i]);
			if(
					current[0].equals(inputId) && 
					current[1].equals(inputPass)
					) {
				isLogined = true;
				break;
			}
		}
		System.out.println("hi!!");
		if(isLogined) {
			System.out.println("Admin");
		}else {
			System.out.println("Who are you??");
		}
		

	}

}
