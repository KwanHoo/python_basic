// 클래스 선언부
public class Hello { //클래스 이름은 소스파일명과 동일해야함
    // 메소드 선언부 main(): 메인 메소드를 프로그램 실행 진입점(entry point)
    public static void main(String[] args) {
        // 콘솔에 출력하는 실행문
        // 실행문 종류 : 변수선언, 값 저장, 메소드 호출
        System.out.println("Hello, Java");
// 컴파일러는 세미클론(;) 까지 하나의 실행문으로 해석
        int x;
        int y;
        x=2000;
        y=400;
        int result = x+y;
        System.out.println(result);

    }// end of main
}// end of class


// src : source
// bin : binary
// 라인주석
/* 범위 주석*/
// 주석은 코드 내 어디서든 작성이 가능, 문자열 내부에서는 작성하면 안됨