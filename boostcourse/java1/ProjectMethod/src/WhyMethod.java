
public class WhyMethod {
	public static void printTwoTimesA() {
		System.out.println("-");
		System.out.println("a");
		System.out.println("b");
	}
	// args : 사용자가 시작할때 주입해주는
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		printTwoTimesA();
		//1억
		twoTimes("a", "*");
		
		// 1억
		printTwoTimesA();
		// 1억
		printAddTimesB("add", "***"); //인자(argument)
	}									// 매개변수(파라미터) parameter
	public static void printAddTimesB(String text, String delimiter) {
		System.out.println(delimiter); //delimiter : 구분자
		System.out.println(text);
		System.out.println(text);
	}
	
	public static String twoTimes(String text, String delimiter) {
		String out ="";
		out = out + delimiter + "\n";
		out = out + text + "\n";
		out = out + text + "\n";
		return out;
		
	}
}
