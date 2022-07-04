
public class AuthApp {

	public static void main(String[] args) {

		System.out.println(args[0]);
		System.out.println(args[1]);
		String id = "hwankko";
		String inputId = args[0];
		
		String pass = "1111";
		String inputPass = args[1];
		
		System.out.println("hi.");
//		if(inputId == id) {
//		if(inputId.equals(id)) {
//			if(inputPass.equals(pass)) {
//				System.out.println("Master");
//			}else {
//				System.out.println("Wrong Password");
//			}
//		}else {
//			System.out.println("Who are you??");
//		}
		
		// 논리연산자
		if(inputId.equals(id) && inputPass.equals(pass)) {
			System.out.println("Master~~~");
		}else {
			System.out.println("Who are you??");
		}
	}

}
