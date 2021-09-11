// 변수
// 변수 선언 : 변수에 어떤 타입(자료형)의 데이터를 저장할 것인지, 변수 이름이 무엇인지 결정
/* int x; int y;
   int x, y;   동일
 */
// 변수이름 : 자바는 영어 대소문자 구분, 첫문자는 영어 소문자로 시작
// 선언과 생성은 다른이야기 : 변수에 값이 저장되지 않으면 변수가 생성되지 않음
// 변수에 최초로 값이 저장될 때 변수가 생성됨(변수 초기화)/이때 사용된값(초기값)
// int score = 2400;  변수가 초기화되면 메모리 번지 정보를 갖게됨, 해당 메모리 번에 값이 저장됨

public class variable {
    public static void main(String[] args){
        int value = 2000;

        int result = value + 400;

        System.out.println(result);

        int hour = 12;
        int minute = 30;
        System.out.println(hour + "시간" + minute +"분");
        int totalMinute= (hour*60)+minute;
        System.out.println("총"+totalMinute+"분");

        // variable excahnge(swap)

        int h = 2000;
        int g = 400;
        System.out.println("h:"+h+", g:"+g);

        int temp = h;
        h = g;
        g = temp;
        System.out.println("h:"+h+", g:"+g);


        // 변수 사용 범위
        /*
        int v1 = 15;
        if(v1>10){
            int v2;
            v2=v1-10;
        }
        int v3= v1+v2 +5;   #v2가 if{}내에 선언이 되어 있어서 v2값을 얻을수없다는 에러가뜸
*/
    }
}
