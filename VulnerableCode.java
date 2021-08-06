import java.util.*;

public class VulnerableCode {
	public static void main(String[] args) {
		String input;
		Scanner sc = new Scanner (System.in);
		String password = "Open";
		System.out.println("Enter password to login");
		input = sc.nextLine();
		if(input == password)
		{
			System.out.println("Logged in successfully");
		}
		else
		{
			System.out.println("Wrong credentials, exiting!!");
			System.exit(0);
		}
	}
}




