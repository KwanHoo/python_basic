class Greeting{
	public static void hi() {
		System.out.println("hi");
	}
	private static void h2i() {
		System.out.println("hi");
	}
}


public class AccessLevelModifiersMethod {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Greeting.hi();
		//Greeting.h2i();  -> error
	}

}
