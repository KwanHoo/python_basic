
public class AccountingApp {
	// 공급가액
	public static double valueOfSupply = 10000.0;
	
	// 부가가치세율
	public static double vatRate = 0.1;
	
	public static double getVat() {
		return valueOfSupply * vatRate;
	}
	
	public static double getTotal() {
		return valueOfSupply + getVat();
	}
	
	public static void main(String[] args) {

		// 부가세
		//double vat = valueOfSupply * vatRate;
		//double vat = getVat();
		
		// 합계
		//double total = valueOfSupply + vat;
		//double total = getTotal();
		
		
		System.out.println("Value of supply : " + valueOfSupply);
		//System.out.println("VAT : " + vat );
		System.out.println("VAT : " + getVat() );
		//System.out.println("Total : " + total);
		System.out.println("Total : " + getTotal());
	}

}
