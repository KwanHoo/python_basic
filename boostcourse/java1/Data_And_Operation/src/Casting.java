
public class Casting {

	public static void main(String[] args) {
		
		double a = 1.1;
		double b = 1;
		double b2 = (double) 1;
		System.out.println(b); // 더블형이기 때문에 실수로 컨버팅
		
		
//		int c = 1.21;
		double d = 1.21;
		int e = (int) 1.21;
		System.out.println(e);
		
		// 1 to string
		String strI = Integer.toString(314);
		System.out.println(strI);
		System.out.println(strI.getClass());


	}

}
