import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;

public class langStat{
	public static void main(String[] args) {
		

		String file = "../files/output_final.txt";


		averages(file);
		System.out.println("Average people per conversation: " + peoplePerConvo(file) );
		numPeople(file);


	}

	public static double peoplePerConvo(String file){

		double people_per_convo;
		
		try{

			String file_name = file;
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);


			String file_line = br.readLine();
			String[] split_file = file_line.split("<s>");

			int[] ppc = new int[split_file.length];

			ArrayList<Integer> convo_nums = new ArrayList<Integer>();

			//look at each conversation
			for(int i = 0; i < split_file.length; i++){

				String convo = split_file[i];
				ArrayList<Integer> id_list = new ArrayList<Integer>();

				for(int j = 0; j < convo.length()-3; j++){

					//found id tag in convo
					if(convo.charAt(j) == 'u' && convo.charAt(j+1) == 'i' && convo.charAt(j+2) == 'd' && convo.charAt(j+3) == '='){
						int m = j+5;
						String id_string = "";
						while(Character.isDigit(convo.charAt(m))){
							id_string += convo.charAt(m);
							m++;
						}

						int id = Integer.parseInt(id_string);
						if(id_list.contains(id) == false){
							id_list.add(id);
						}
					}
				}
				convo_nums.add(id_list.size());
			}

			double average = 0;
			for(int i = 0; i < convo_nums.size(); i++){
				average += (double)convo_nums.get(i);
			}

			average = average / (convo_nums.size()-1);
			people_per_convo = average;

		}


		catch(Exception e){
			people_per_convo = -1;
			System.out.println("Error in peoplePerConvo: " + e);
		}

		return people_per_convo;

	}


	public static void numPeople(String file){
		try{

			String file_name = file;
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);

			String file_line = br.readLine();
			String id_string = "";
			int max_id = 0;
			int count = 0;

			for(int i = 0; i < file_line.length()-3; i++){
				//Find a <utt uid="xxxx" thing
				if(file_line.charAt(i) == 'u' && file_line.charAt(i+1) == 'i' && file_line.charAt(i+2) == 'd' && file_line.charAt(i+3) == '='){
					int j = i+5;
					while(Character.isDigit(file_line.charAt(j))){
						id_string += file_line.charAt(j);
						j++;
						
					}
					if(id_string != ""){
						if(Integer.parseInt(id_string) > max_id){
							max_id = Integer.parseInt(id_string);
						}
					}
					id_string = "";
				}
			}
			System.out.println("Number of people: " + max_id + "\n\n");
		}
		catch(Exception e){
			System.out.println("Error in 'numPeople': " + e);
		}
	}


	public static void averages(String file){
		try{

			String file_name = file;
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);

			int word_count = 0;
			int convo_count = 0;
			int utt_count = 0;

			String file_line = br.readLine();
			for(int i = 0; i < file_line.length()-2; i++){
				//cound number of words
				if(Character.isWhitespace(file_line.charAt(i))){
					word_count++;
				}
				//count number of convos
				if(file_line.charAt(i) == '<' && file_line.charAt(i+1) == 's' && file_line.charAt(i+2) == '>'){
					convo_count++;
				}
				//count number of utterances
				if(file_line.charAt(i) == '<' && file_line.charAt(i+1) == 'u' && file_line.charAt(i+2) == 't'){
					utt_count++;
				}
			}

			System.out.println("\n\nNumber of words: " + word_count);
			System.out.println("Number of conversations: " + convo_count);
			
			System.out.println("Average number of turns per convo: " + (double)utt_count/convo_count);

		}
		catch(Exception e){
			System.out.println("Error in 'averages': " + e);
		}
	}
}