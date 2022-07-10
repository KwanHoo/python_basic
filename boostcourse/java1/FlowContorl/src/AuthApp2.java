
public class AuthApp2 {

	public static void main(String[] args) {

		System.out.println(args[0]);
		System.out.println(args[1]);
		String id = "hwankko";
		String inputId = args[0];
		
		String pass = "1111";
		String pass2 = "2222";
		String inputPass = args[1];
		
		System.out.println("hi.");

		
		boolean isRightPass = (inputPass.equals(pass) || inputPass.equals(pass2));
		if(inputId.equals(id) && isRightPass) {
			System.out.println("Master~~~");
		}else {
			System.out.println("Who are you??");
		}
	}

}
