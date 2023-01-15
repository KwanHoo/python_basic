import java.io.FileWriter;
import java.io.IOException;

public class OthersOOP {

	public static void main(String[] args) throws IOException {
		// 일회용으로 사용되는거
		// 클래스로 그대로 이용함
		// class: System, Math, FileWriter
		// instance : f1, f2
		
		System.out.println(Math.PI);
		System.out.println(Math.floor(1.7));
		System.out.println(Math.ceil(2.6));
		
		// 클래스를 직접사용하는 것이 아니라
		// 클래스를 복제해서 인스턴스로 만들어서 제어함
		FileWriter f1 = new FileWriter("data.txt");
		f1.write("Hello");
		f1.write(" JAVA");
		f1.close();
		
		FileWriter f2 = new FileWriter("data2.txt");
		f2.write("Hello");
		f2.write(" JAVA2");
		f2.close();
				
		
	}

}
