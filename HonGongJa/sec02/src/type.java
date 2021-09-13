// 자바 변수 타입(자료형)
// 변수를 선언할 떄 주어지는 타입에 따라 변수에 저장할 수 있는 값의 종류와 허용 범위가 달라짐

// 타입의 종류, 허용범위

//정수 타입 : byte, char, short, int, long
//실수 타입 : float, double
//논리 타입 : boolean

// 리터럴(literal) : 소스코드에서 프로그래머에 의해 직접 입력되는 값
// 2진수 : 0b or 0B로 시작하고 0,1로 구성
// 8진수 : 0 으로 시작하고 0~7 숫자로 구성
// 10진수 : 소수점이 없는 0~9 숫자로 구성
// 16진수 : 0x or 0X로 시작하고 0~9 숫자와 A,B,C,D,E,F 또는 a,b,c,d,e,f로 구성
public class type {
    public static void main(String[] args){
        // 정수 리터럴
        int vint1 = 0b1011;     // 2진수
        int vint2 = 0206;       // 8진수
        int vint3 = 365;        //10진수
        int vint4 = 0xB3;       //16진수

        System.out.println("int1 : "+ vint1);
        System.out.println("int2 : "+ vint2);
        System.out.println("int3 : "+ vint3);
        System.out.println("int4 : "+ vint4);


        // byte type 변수
        //  -128 ~ 127

        byte vbyte1 = -128;
        byte vbyte2 = 127;
//        byte vbyte3 = 128;  컴파일에러 (type mismatch)

        System.out.println("byte1 : "+ vbyte1);
        System.out.println("byte2 : "+ vbyte2);

        // 기본적으로 컴파일러는 정수 리터럴을 int 타입으로 간주
        // long 타입 : int type의 허용범위 초과할경우 long타입임을 컴파일러에게 알려줘야함 (L,l)

        long vlong1 = 10;
        long vlong2 = 20L;
//        long vlong3 = 10000000000;  컴파일 에러
        long vlong4 = 10000000000L;

        System.out.println("long1 : "+ vlong1);
        System.out.println("long2 : "+ vlong2);
        System.out.println("long4 : "+ vlong4);

        // char 타입 '' -> 유니코드로 저장= 숫자( 정수타입)

        char vchar1 = 'A';          //문자
        char vchar2 = 65;           //10진수
        char vchar3 = '\u0041';     //16진수

        char vchar4 = '가';
        char vchar5 = 44032;
        char vchar6 = '\uac00';

        System.out.println(vchar1);
        System.out.println(vchar2);
        System.out.println(vchar3);
        System.out.println(vchar4);
        System.out.println(vchar5);
        System.out.println(vchar6);

        // String type ""
        String name = "hwankko";
        String job = "프로그래머";
        System.out.println(name);
        System.out.println(job);
/*
이스케이프 문자
\t
\n
\r 캐리지 리턴
\"
\'
\\
\\ u16진수 16진수 유니코드에 해당하는 문자
 */
        // 실수 타입 (float 타입. double 타입)

        //float vfloat1 = 3.14; 컴파일 에러
        float vfloat2 = 3.14f;
        double vdouble3 = 3.14;

        // 정밀도 테스트
        // float : 7자리
        // double : 15자리

        System.out.println("float2 : "+vfloat2);
        System.out.println("float3 : "+vdouble3);

        // e 사용하기
        double ve4 = 3e6;   //3.0 * 10^6
        float ve5= 3e6F;
        double ve6 = 2e-3;  //2.0 * 10^-3

        System.out.println("ve4 : " + ve4);
        System.out.println("ve5 : " + ve5);
        System.out.println("ve6 : " + ve6);


        boolean stop = true;
        if (stop) {
            System.out.println("중지합니다");
        }else{
            System.out.println("시작합니다.");
        }


        // 자동 타입 변환 (promotion)
        // 기본 타입을 허용 범위 크기순으로 정리 : byte<short<int<long<float<double

        // 강제 타입 변환 (casting)
        // 큰 허용 범위 타입을 작은 허용 범위 타입으로 강제로 나눠서 저장
        // 작은허용 범위 타입 = (작은 허용 범위타입) 큰허용 범위 타입



    }

}
