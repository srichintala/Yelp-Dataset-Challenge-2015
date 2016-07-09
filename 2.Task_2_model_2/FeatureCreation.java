/* This program generates frequency count for each
 * feature generated through feature generation program.
 * This program computes frequencies for both bigrams 
 * as well as unigrams. In experiment feature frequencies were 
 * also generated for individual unigrams and bigrams
 * Author : Nayana Charwad
 * */

package processReviews;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.StringReader;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.core.StopAnalyzer;
import org.apache.lucene.analysis.en.PorterStemFilter;
import org.apache.lucene.analysis.shingle.ShingleFilter;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;

public class FeatureCreation {

	public static void main(String[] args) throws IOException {
		
		String featurePath = "/Users/Nayana/Desktop/Data/Features.csv";
		FileReader featureInput = new FileReader(featurePath);
		BufferedReader featureReader = new BufferedReader(featureInput);		
		
		FileWriter output = new FileWriter("/Users/Nayana/Desktop/OutputTrainBi.csv");
		BufferedWriter outputWriter = new BufferedWriter(output);	
		
		HashMap<String,Integer> countMap = new HashMap<String,Integer>();
		HashMap<Integer,String> indexMap = new HashMap<Integer,String>();
		String line = null;
		int lineCount = 0;
		int countFeatures = 1096;
		
		//Get input features from generated feature file
		while(((line = featureReader.readLine())!=null) && lineCount < countFeatures)
		{
			if(!countMap.containsKey(line))
			{
	        	countMap.put(line, 0);	
	        	indexMap.put(lineCount, line);
	        	outputWriter.write(line + ",");
	        	lineCount++;
			}
		}
		outputWriter.write("stars");
		featureReader.close();
		
		//read input file containing review text
		String filePath = "/Users/Nayana/Desktop/Data/InputTrain.csv";
		FileReader input = new FileReader(filePath);
		BufferedReader inputReader = new BufferedReader(input);		
		lineCount = 0;
	    String user = "",review = "",business="",stars="";
	    boolean newRecord = false;
	    int stop = 0;
	    
		while((line = inputReader.readLine())!=null && stop < 10000)
		{
			//write feature frequencies for each individual review record
			if(line.contains("STARTRECORD"))
			{
				if(newRecord)
				{
					outputWriter.write("\n");
					stop++;
					for(int i=0;i<countFeatures;i++)
					{
						outputWriter.write(countMap.get(indexMap.get(i)) + ",");
						countMap.put(indexMap.get(i),0);
					}
					outputWriter.write(stars);
				}
				
				String[] fields = line.split(",");
				user = fields[1];
				review = fields[2];
				business = fields[3];
				stars = fields[4];
				newRecord = true;
			}
			
			//Unigram features
			//Remove stop words and genrate unigram tokens
			Analyzer analyzer = new StopAnalyzer();
			TokenStream tokenStream = analyzer.tokenStream("contents", new StringReader(line));
			tokenStream = new PorterStemFilter(tokenStream);
		    CharTermAttribute charTermAttribute = tokenStream.addAttribute(CharTermAttribute.class);
		    tokenStream.reset();
		    
		    //count frequencies for each feature
		    while (tokenStream.incrementToken()) {
		        String term = charTermAttribute.toString();
		        
		            if(countMap.containsKey(term))
			        {
			        	int oldCount = countMap.get(term);
			        	countMap.put(term, oldCount+1);
			        }
		    }
		    
		    analyzer.close();
		    tokenStream.close();
		    
		    //Bigram features
		    //Remove stop words
		    Analyzer analyzerb = new StopAnalyzer();
		    TokenStream tokenStreamb = analyzerb.tokenStream("contents", new StringReader(line));
			tokenStreamb = new PorterStemFilter(tokenStreamb);
			//generate bigram tokens and count frequencies of input features
			ShingleFilter sf = new ShingleFilter(tokenStreamb,2,2);
			sf.setOutputUnigrams(false);
			
			CharTermAttribute charTermAttributeb = sf.addAttribute(CharTermAttribute.class);
		    sf.reset();
		    
		    while (sf.incrementToken()) {
		        String term = charTermAttributeb.toString();
		        
		            if(countMap.containsKey(term))
			        {
			        	int oldCount = countMap.get(term);
			        	countMap.put(term, oldCount+1);
			        }
		    }
		    
		    analyzerb.close();
		    sf.close();
		    tokenStreamb.close();
		    
		    lineCount++;
		    if((lineCount % 100000)==0)
		    {
		    	System.out.println("Processed Lines : " + lineCount);
		    }
		}
		
		inputReader.close();
	    outputWriter.close();
	}
}
