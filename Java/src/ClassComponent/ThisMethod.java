package ClassComponent;

class A {
	int m1, m2, m3, m4;
	A(){
		m1 = 1;
		m2 = 2;
		m3 = 3;
		m4 = 4;
	}
	A(int a){
		m1 = a;
		m2 = 2;
		m3 = 3;
		m4 = 4;
	}
	A(int a, int b){
		m1 = a;
		m2 = b;
		m3 = 3;
		m4 = 4;
	}
	void print() {
		System.out.println(m1 + " ");
		System.out.println(m2 + " ");
		System.out.println(m3 + " ");
		System.out.println(m4 + " ");
		System.out.println();
	}
}

class I{
	int m1, m2, m3, m4;
	I(){
		m1 = 1;
		m2 = 2;
		m3 = 3;
		m4 = 4;
	}
	I(int a){
		this();
		m1 = a;
		
	}
	I(int a, int b){
		this(a);
		m2 = b;
	}
	void print() {
		System.out.println(m1 + " ");
		System.out.println(m2 + " ");
		System.out.println(m3 + " ");
		System.out.println(m4 + " ");
		System.out.println();
	}
}

public class ThisMethod {

	public static void main(String[] args) {
		A a1 = new A();
		A a2 = new A(10);
		A a3 = new A(10, 20);
		a1.print();
		a2.print();
		a3.print();
		System.out.println();
		
		I b1 = new I();
		I b2 = new I(10);
		I b3 = new I(10, 20);
		b1.print();
		b2.print();
		b3.print();

	}

}
