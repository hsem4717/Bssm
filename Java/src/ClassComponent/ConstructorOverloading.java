package ClassComponent;

class H{
	H(){
		System.out.println("첫 번째 생성자");
	}
	H(int a){
		System.out.println("두 번째 생성자");
	}
	H(int a, int b){
		System.out.println("세 번째 생성자");
	}
}

public class ConstructorOverloading {

	public static void main(String[] args) {
		
		H a1 = new H();
		H a2 = new H(3);
		H a3 = new H(3, 5);
	

	}

}