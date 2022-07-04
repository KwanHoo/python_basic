
public class AccountingArrayLoopApp {

	public static void main(String[] args) {
		
		double valueOfSupply = Double.parseDouble(args[0]);
		double vatRate = 0.1;
		double expenseRate = 0.3;
		double vat = valueOfSupply * vatRate;
		double total = valueOfSupply + valueOfSupply*vatRate;
		double expense =  valueOfSupply * expenseRate;
		double income = valueOfSupply - expense;
		
		double[] dividendRate = new double[3];
		dividendRate[0] = 0.5;
		dividendRate[1] = 0.3;
		dividendRate[2] = 0.2;


		System.out.println("Value of supply : " + valueOfSupply);
		System.out.println("VAT : " + vat );
		System.out.println("Total : " + total);
		System.out.println("Expense : " + expense);
		System.out.println("Income : "+income);


		
		int i = 0;
		while (i < dividendRate.length) {
			System.out.println("Dividend  : " + (income * dividendRate[i]));
			i = i + 1;
		}


	}

}
