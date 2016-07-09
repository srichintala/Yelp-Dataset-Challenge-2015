package YelpCategoryPrediction.QueryGeneratorModule;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import YelpCategoryPrediction.Constants.*;

/**
 * @author Renuka
 * Class for file operations
 */


public class FileAccess {

	private String indexFile;
	private String queryFile;
	private String workingFile;
	
	public String getIndexFile() {
		return indexFile;
	}


	public void setIndexFile(String indexFile) {
		this.indexFile = indexFile;
	}


	public String getQueryFile() {
		return queryFile;
	}


	public void setQueryFile(String queryFile) {
		this.queryFile = queryFile;
	}


	public String getWorkingFile() {
		return workingFile;
	}


	public void setWorkingFile(String workingFile) {
		this.workingFile = workingFile;
	}


	public FileAccess(){
		indexFile = Constants.indexFile;
		queryFile = Constants.queryFile;
		workingFile = Constants.workingFile;
	}
	
	
	/**
	 * Function to write string to file
	 * @param filename - absolute file name
	 * @param text - text to be written to file
	 */
	public void WriteToFile(String filename, String text) {
		deleteFile(filename);
		
		try {
	         BufferedWriter out = new 
	         BufferedWriter(new FileWriter(filename));
	         out.write(text);
	         out.close();
	         System.out.println
	         ("File created successfully");
	      }
	      catch (IOException e) {
	      }
	}

	/**
	 * Function to delete a file
	 * @param filename - absolute file name
	 */
	public void deleteFile(String filename) {

		try {

			File file = new File(filename);

			if (file.delete()) {
				System.out.println(file.getName() + " is deleted!");
			} else {
				System.out.println("Delete operation is failed.");
			}

		} catch (Exception e) {

			e.printStackTrace();

		}

	}

	/**
	 * Function to read lines from file into an arraylist
	 * @param filename - absolute file name
	 * @return - list of lines read from file
	 */
	public ArrayList<String> ReadFromFile(String filename) {
		ArrayList<String> lines = new ArrayList<String>();
		try {
			BufferedReader in = new BufferedReader(new FileReader(filename));
			String str;
			while ((str = in.readLine()) != null) {
				lines.add(str);
			}
			// lines.add(str);
		} catch (IOException e) {
		}
		return lines;
	}

	/**
	 * Function to append to file
	 * @param filename - absolute file name
	 * @param line - line to be append to file
	 */
	public void AppendAtEnd(String filename, String line) {
		try {
			BufferedWriter out = new BufferedWriter(new FileWriter(filename,
					true));
			out.write(line);
			out.close();

		} catch (IOException e) {
			System.out.println("exception occoured" + e);
		}
	}

}
