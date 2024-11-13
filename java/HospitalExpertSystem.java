// 10. Develop an Expert system for a Hospital or any suitable application.

import java.util.*;
public class HospitalExpertSystem{
	private Map<String, String> rules;
	
	public HospitalExpertSystem(){
		this.rules= new HashMap<>();
		
		rules.put("fever and cough", "Pneumonia");
		rules.put("fever and headache", "Malaria");
		rules.put("cough and chest pain", "Bronchitis");
		rules.put("headache and fatigue", "Viral Infection");
	}

	public String diagnose(String symptoms){
		for(Map.Entry<String, String> entry : rules.entrySet()){
			if(symptoms.contains(entry.getKey())){
				return entry.getValue();
			}
		}
		return "Unknown diagnosis";
	}
	
	public static void main(String args[]){
		HospitalExpertSystem HES = new HospitalExpertSystem();
		Scanner sc = new Scanner(System.in);
		System.out.println("Welcome to Hospital Expert System!");
		System.out.println("Type 'quit' to stop diagnosing.");
		
		while(true){
			System.out.print("Enter symptoms (seperate with and) : ");
			String symptoms = sc.nextLine();
			
			if(symptoms.equalsIgnoreCase("quit")){
				break;
			}
			System.out.println("Diagnosis : " + HES.diagnose(symptoms));
		}
	}
}
