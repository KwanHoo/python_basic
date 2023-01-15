class Print{
	
	public String delimiter;
	// 메소드가 인스턴스의 소속일 떄는 static을 빼주어야함
	public void a() {
		System.out.println(this.delimiter);
		System.out.println("a");
		System.out.println("a");
	}
	public void b() {
		System.out.println(this.delimiter);
		System.out.println("b");
		System.out.println("b");
	}
}


public class staticMethod {
	// 메소드가 클래스의 소속 일때는 static이 있어야함
	public static void main(String[] args) {
		
//		Print.a("--");
//		Print.b("==");
		
		// instance
		Print t1 = new Print();
		t1.delimiter = "-=";
		t1.a();
		t1.b();
		
		Print t2 = new Print();
		t2.delimiter = "**";
		t2.a();
		t2.b();
	}


}
