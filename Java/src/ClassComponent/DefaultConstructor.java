package ClassComponent;

class D{
	int m;
	void work() {
		System.out.println(m);
	}
	//기본 생성자 자동 추가
}
class B{
	int m;
	void work() {
		System.out.println(m);
	}
	B(){
		
	}
}
class C{
	int m;
	void work() {
		System.out.println(m);
	}
	C(int a){
		m = a;
	}
}

public class DefaultConstructor {
	public static void main(String[] args) {
		D a = new D();
		B b = new B();
		C c = new C(3);
		
		a.work();
		b.work();
		c.work();
		
		

	}

}
